from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Listing(models.Model):
    class Meta:
        ordering = ['-created_at']
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='listings')
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ListingImage(models.Model):
    url = models.ImageField(upload_to='listing_images/')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='images')
