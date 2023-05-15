from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm

# top page
def products(request):
    products = Product.objects.all() 
    context = {'products': products}
    return render(request, 'products/products.html', context)

# product detail
def detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/detail.html', context)

# add new product
def add_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)

# update product
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)

# delete product
def delete_product(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('profile')

    context = {'object': product}
    return render(request, 'products/delete_product.html', context)