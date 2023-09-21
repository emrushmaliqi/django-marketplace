from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms-conditions', views.terms_conditions, name='terms-conditions'),
    path('category/<str:slug>', views.category, name='category'),
    path('listing/<int:id>', views.show_listing, name='listing'),
    path('listing/create', views.create_listing, name='create-listing'),
    path('listing/edit/<int:id>', views.edit_listing, name='edit-listing'),
    path('listing/delete/<int:id>', views.delete_listing, name='delete-listing'),
    path('/profile/<int:id>', views.profile, name='profile'),
]
