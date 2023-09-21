from django.db import models
from django.contrib.auth import get_user_model
from listings.models import Listing

# Create your models here.


class Message(models.Model):
    class Meta:
        ordering = ['created_at']
    text = models.CharField(max_length=300)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='messages')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='messages')
    seller_message = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
