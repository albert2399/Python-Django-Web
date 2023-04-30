from django.shortcuts import render, redirect
from .carro import Carro
from comprar.models import Producto


# Create your views here.

def agregar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
    
    return redirect('Comprar')


def eliminar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.delete(producto=producto)
    
    return redirect('Comprar')


def restar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.restar(producto=producto)
    
    return redirect('Comprar')


def vaciar_carro(request):
    
    carro = Carro(request)
    
    carro.vaciar()
    
    return redirect('Comprar')



