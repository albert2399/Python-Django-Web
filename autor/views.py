from django.shortcuts import render
from autor.models import Foto

# Create your views here.

def fotos(request):
    
    fotos = Foto.objects.all()
    
    return render(request, 'autor.html', {'fotos': fotos})