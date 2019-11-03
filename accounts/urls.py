from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('registro/', views.register, name='accounts_register'),
]