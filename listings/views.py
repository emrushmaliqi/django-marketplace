from django.shortcuts import render
from .models import Category, Listing
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

    listings = Listing.objects.filter(category=category)[:20]

    context = {'categories': categories,
               'category': category, 'listings': listings}
    return render(request, 'category.html', context)
