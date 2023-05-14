from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm

# Create your views here.
def products(request):
    products = Product.objects.all() 
    context = {'products': products}
    return render(request, 'products/products.html', context)

def detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/detail.html', context)

def add_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)