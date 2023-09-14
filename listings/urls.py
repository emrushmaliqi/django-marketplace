from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms-conditions', views.terms_conditions, name='terms-conditions'),
    path('category/<str:slug>', views.category, name='category'),
]
