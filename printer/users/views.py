from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForms

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')