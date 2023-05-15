from django.shortcuts import render

from products.models import Product

def user_login(request):
    context = {}
    return render(request, 'users/login_register.html', context)



# user profile page
def profile(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'users/profile.html', context)