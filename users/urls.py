from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('', views.profile, name='profile'),
]