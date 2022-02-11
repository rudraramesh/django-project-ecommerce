from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Product
from . forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def testFunc(request):
    return HttpResponse('this is the test function in python django')


def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'PRODUCT ADDED')
            return redirect('/products/addproduct')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Please verify forms fields')
            return render(request, 'products/addproduct.html', {
                'form': form
            })

    context = {
        'form': ProductForm
    }
    return render(request, 'products/addproduct.html', context)


def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'CATEGORY ADDED')
            return redirect('/products/addcategory')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Please verify forms fields')
            return render(request, 'products/addcategory.html', {
                'form': form
            })

    context = {
        'form': CategoryForm
    }
    return render(request, 'products/addcategory.html', context)


def update_product(request, product_id):
    instance = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'PRODUCT ADDED')
            return redirect('/products')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Please verify forms fields')
            return render(request, 'products/updateproduct.html', {
                'form': form
            })
    context = {
        'form': ProductForm(instance=instance)
    }

    return render(request, 'products/updateproduct.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, 'PRODUCT DELETED')
    return redirect('/products')


def show_category(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'products/allcategory.html', context)