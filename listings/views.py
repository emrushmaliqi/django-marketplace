from django.shortcuts import render, redirect
from .models import Category, Listing
from django.db.models import Q
from .forms import ListingForm, ListingEditForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    categories = Category.objects.all()

    return render(request, 'home.html', {'categories': categories})


def terms_conditions(request):
    categories = Category.objects.all()
    return render(request, 'terms-conditions.html', {'categories': categories})


def category(request, slug):
    categories = Category.objects.all()

    category = Category.objects.get(slug=slug)

    listings = Listing.objects.filter(
        ~Q(user=request.user), category=category)[:20]

    context = {'categories': categories,
               'category': category, 'listings': listings}
    return render(request, 'category.html', context)


def show_listing(request, id):
    listing = Listing.objects.get(id=id)
    images = listing.images.all()
    categories = Category.objects.all()

    context = {'listing': listing, 'images': images, 'categories': categories}
    return render(request, 'listing/show-listing.html', context)


def create_listing(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user_id = request.user.id
            listing.save()
            if request.FILES.getlist('images'):
                for image in request.FILES.getlist('images'):
                    listing.images.create(url=image)

            return redirect('profile', id=request.user.id)
        return render(request, 'listing/create-listing.html', {'form': form, 'categories': categories})

    form = ListingForm()

    context = {'form': form, 'categories': categories}
    return render(request, 'listing/create-listing.html', context)


def edit_listing(request, id):
    categories = Category.objects.all()
    try:
        listing = Listing.objects.get(id=id)
    except ObjectDoesNotExist:
        return redirect('home')
    if request.user.id != listing.user_id:
        return redirect('home')
    if request.method == 'POST':
        form = ListingEditForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user_id = request.user.id
            listing.save()
            if 'deleted_images' in request.POST:
                for image in request.POST['deleted_images'].split(','):
                    listing.images.get(id=image).delete()
                    print(image)
            if request.FILES.getlist('images'):
                for image in request.FILES.getlist('images'):
                    listing.images.create(url=image)

            return redirect('profile', id=request.user.id)
        return render(request, 'listing/edit-listing.html', {'form': form, 'categories': categories})

    form = ListingEditForm(instance=listing)

    context = {'form': form, 'listing': listing, 'categories': categories}
    return render(request, 'listing/edit-listing.html', context)


def delete_listing(request, id):
    listing = Listing.objects.get(id=id)
    if listing.user.id == request.user.id:
        listing.delete()
    return redirect('profile', id=request.user.id)


def profile(request, id):
    user = get_user_model().objects.get(id=id)
    categories = Category.objects.all()

    context = {'user': user, 'categories': categories}
    return render(request, 'profile.html', context)
