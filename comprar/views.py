from django.shortcuts import render
from comprar.models import Producto
from carro.carro import Carro
from carro.views import vaciar_carro

def comprar(request):
    
    productos = Producto.objects.all()
    return render(request, 'comprar.html', {"productos": productos})
