from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm

# Create your views here.


class Register(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})
