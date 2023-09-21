from .models import Listing, Category
from django import forms


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'price', 'description', 'category']

    title = forms.CharField(
        max_length=40, min_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

    price = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    description = forms.CharField(
        max_length=1000, min_length=10, widget=forms.Textarea(attrs={'class': 'form-control'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}))


class ListingEditForm(ListingForm):
    class Meta:
        model = Listing
        fields = ['title', 'price', 'description', 'category', 'is_sold']
