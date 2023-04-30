from django.shortcuts import render, HttpResponse

from wormgateWeb.models import Personaje


# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def personajes(request):
    
    personajes = Personaje.objects.all()
    
    return render(request, 'personajes.html', {'personajes': personajes})


def capitulo(request):
    
    return render(request, 'capitulo1.html')