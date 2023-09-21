from django.shortcuts import render, redirect
from .models import Message
from listings.models import Listing, Category
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth import get_user_model
# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    categories = Category.objects.all()
    purchases = find_purchases(request.user)
    sales = find_sales(request.user)

    context = {'purchases': purchases,
               'sales': sales, 'categories': categories}
    return render(request, 'messaging/messages.html', context)


def find_purchases(user):
    purchases = user.messages.values(
        'listing').annotate(message_count=Count('listing')).values_list('listing', flat=True).order_by()

    return Listing.objects.filter(id__in=purchases, is_sold=False)


def find_sales(user):
    listings = Listing.objects.filter(user=user, is_sold=False)
    sales_indexes = Message.objects.filter(listing__in=listings).values(
        'listing', 'user').annotate(Count('listing'), Count('user')).values('listing', 'user').order_by()
    sales = []

    class Sale:
        def __init__(self, listing, user):
            self.listing = listing
            self.user = user

        def last_message(self):
            return self.listing.messages.filter(user=self.user).order_by('-created_at').first()

    for d in sales_indexes:
        user = get_user_model().objects.get(id=d['user'])
        listing = Listing.objects.get(id=d['listing'])
        sales.append(Sale(listing, user))

    for p in sales:
        print(p.listing.images.first().get_absolute_url())
    return sales


@login_required(login_url='/auth/login')
def message_buy(request, id):
    try:
        listing = Listing.objects.get(id=id)
    except ObjectDoesNotExist:
        listing = None
    if listing is None:
        return redirect('home')

    if listing.is_sold or listing.user.id == request.user.id:
        return redirect('/listing/' + str(id))

    if (request.method == 'POST'):
        message_text = request.POST['message']
        if (len(message_text) > 0):
            message = Message(text=message_text,
                              listing_id=id, user=request.user)
            message.save()
        return redirect('/messages/listing/' + str(id))

    categories = Category.objects.all()

    messages = Message.objects.filter(listing=listing, user=request.user)

    context = {'messages': messages,
               'listing': listing, 'categories': categories}
    return render(request, 'messaging/buy-chat.html', context)


@login_required(login_url='/auth/login')
def message_sell(request, listing_id, user_id):
    try:
        listing = Listing.objects.get(id=listing_id)
    except ObjectDoesNotExist:
        listing = None
    if listing is None:
        return redirect('home')

    if listing.is_sold or listing.user.id != request.user.id or listing.messages.filter(user=user_id).count() == 0:
        return redirect('/listing/' + str(listing_id))

    if (request.method == 'POST'):
        message_text = request.POST['message']
        if (len(message_text) > 0):
            message = Message(text=message_text,
                              listing_id=listing_id, user_id=user_id, seller_message=True)
            message.save()
        return redirect('/messages/listing/' + str(listing_id) + '/user/' + str(user_id))

    categories = Category.objects.all()
    user = get_user_model().objects.get(id=user_id)
    messages = Message.objects.filter(listing=listing, user=user)

    context = {'messages': messages,
               'listing': listing, 'user': user, 'categories': categories}
    return render(request, 'messaging/sell-chat.html', context)
