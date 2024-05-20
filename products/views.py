from django.shortcuts import render
# Create your views here.

from products.models import ProductCategory, ProductFormat, EducationTrans, Product




def index(request):
    context = {
        'title': 'Navigator',
        'categories': ProductCategory.objects.all(),
        'educationFormats': ProductFormat.objects.all(),
        'transEducations': EducationTrans.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/index.html', context)

def products(
        request, 
        category_id=None, 
        educationFormat_id=None, 
        transEducation_id=None):
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    if educationFormat_id:
        educationFormat = ProductFormat.objects.get(id=educationFormat_id)
        products = Product.objects.filter(educationFormat=educationFormat)
    if transEducation_id:
        transEducation = EducationTrans.objects.get(id=transEducation_id)
        products = Product.objects.filter(transEducation=transEducation)
    else:
        products = Product.objects.all()
    context = {
        'title': 'Navigator | Products',
        'categories': ProductCategory.objects.all(),
        'educationFormats': ProductFormat.objects.all(),
        'transEducations': EducationTrans.objects.all(),
        'products': products,
    }
    return render(request, 'products/products.html', context)

def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    context = {
        'title': 'Navigator | Search Results',
        'categories': ProductCategory.objects.all(),
        'educationFormats': ProductFormat.objects.all(),
        'transEducations': EducationTrans.objects.all(),
        'products': products,
    }
    return render(request, 'products/search_results.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})



