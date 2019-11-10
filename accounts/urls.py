from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('registro/', views.register, name='accounts_register'),
    path('alterar-dados/', views.update_user, name='accounts_update_user'),
    path('alterar-senha/', views.update_password, name='accounts_update_password'),
]