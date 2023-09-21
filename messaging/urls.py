from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="messages"),
    path('listing/<int:id>', views.message_buy, name='message-buy'),
    path('listing/<int:listing_id>/user/<int:user_id>',
         views.message_sell, name='message-sell')
]
