from django.shortcuts import render
from catalog.models import Category

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def product_list(request):
    return render(request, 'core/product_list.html')

def product(request):
    return render(request, 'core/product.html')