from django.shortcuts import render

# Create your views here.

from products.models import ProductCategory, Product

def index(request):
    context = {
        'title': 'Navigator',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Navigator | Products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
