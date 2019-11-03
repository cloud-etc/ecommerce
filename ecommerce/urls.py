from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('entrar/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='core/index.html'), name="logout"),
    path('catalogo/', include('catalog.urls'), name='catalog'),
    path('conta/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
]
