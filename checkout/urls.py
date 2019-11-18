from django.contrib import admin
from django.urls import path
from checkout import views

app_name='checkout'

urlpatterns = [
    path('carrinho/adicionar/<slug>', views.create_cartitem, name='create_cartitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    path('finalizando/<int:pk>/pagseguro/', views.pagseguro_view, name='pagseguro_view'),
    path('lista-pedidos/', views.order_list, name='order_list'),
    path('pedido/<int:pk>', views.order_detail, name='order_detail'),
    path('notificacoes/pagseguro/', views.pagseguro_notification,
        name='pagseguro_notification'
    ),

]





