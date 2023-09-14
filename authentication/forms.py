from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    first_name = forms.CharField(
        label='First Name', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    last_name = forms.CharField(
        label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control mb-2'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'}))
