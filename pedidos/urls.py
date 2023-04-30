from django.urls import path
from pedidos import views

urlpatterns = [
    
    path('', views.procesar_pedidos, name='procesar_pedido'),

]
