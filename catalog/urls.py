from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>', views.category, name='category'),
    path('proda/<slug:slug>', views.product, name='product'),
]





