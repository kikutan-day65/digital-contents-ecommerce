from django.shortcuts import render

from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all() 
    context = {'products': products}
    return render(request, 'products/products.html', context)

def detail(request, pk):
    context = {}
    return render(request, 'products/detail.html', context)