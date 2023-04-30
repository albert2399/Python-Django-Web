from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import FormularioContacto

def contacto(request):
    
    formulario = FormularioContacto()
    
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            correo=EmailMessage("Mensaje desde App Django", "Nombre: {} \nCorreo: {}\nMensaje: {}".format(nombre,email,contenido), "",["erensnk998@gmail.com"],reply_to=[email]) 
            
            try:
                correo.send()
                
                return redirect("/contacto/?valido")
            
            except:
                
                return redirect("/contacto/?invalido")
                

    
    return render(request, 'contacto.html', {'formulario': formulario})
