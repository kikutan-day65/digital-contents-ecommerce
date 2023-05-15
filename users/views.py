from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .models import Profile
from products.models import Product

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            print('Username or passwprd is incorrect')

    context = {}
    return render(request, 'users/login_register.html', context)



# user profile page
def profile(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'users/profile.html', context)