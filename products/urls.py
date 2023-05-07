from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('detail/<str:pk>/', views.detail, name='detail'),
]