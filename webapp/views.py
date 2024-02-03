from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User,auth
from django.views import View
from django.contrib import messages
from .forms import PaymentForm


def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def login_page(request):
    return render(request, 'pages/login.html')
   
def register_page(request):
    return render(request, 'pages/register.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

def membership_page(request):
    return render(request, 'pages/membership.html')

def profilelist(request):
    return render(request, 'pages/profile_list.html')



class PaymentView(View):
    template_name = 'pages/payment_form.html'

    def get(self, request, *args, **kwargs):
        form = PaymentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

        return render(request, self.template_name, {'form': form})



