import imp
from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import LoginForm
from products.models import *



def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'ACCOUNT CREATED')
            return redirect('/register')

        else:
            messages.add_message(request, messages.ERROR,
                                 'PLEASE PROVIDE CORRECT DETAILS')
            return render(request, 'users/register.html', {
                'form': form
            })
    context = {
        'form': UserCreationForm
    }
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/admins/dashboard')

                else:
                    return redirect('/')

            else:
                messages.add_message(
                    request, messages.ERROR, 'please provide correct credentials')
                return render(request, 'users/login.html', {
                    'form': form
                })

    form = LoginForm
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')


def homepage(request):
    products = Product.objects.all().order_by('-id')[:8]
    context = {
        'products':products
    }
    return render(request, 'users/index.html',context)
