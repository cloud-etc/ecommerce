from django.contrib import admin
from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.register, name='register'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
]