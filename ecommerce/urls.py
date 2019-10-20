"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ecommerce/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView
from catalog import views as v_catalog

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contact, name='contact'),
    #path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('entrar/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='core/index.html'), name="logout"),
    path('catalogo/', include('catalog.urls'), name='catalog'),
    path('admin/', admin.site.urls),
]
