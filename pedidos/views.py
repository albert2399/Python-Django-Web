from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedidos(request):
    pedido=Pedido.objects.create(usuario=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value['cantidad'],
            usuario=request.user,
            pedido=pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_correo(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
        )
    
    messages.success(request, 'El pedido ha sido procesado correctamente')
    
    return redirect("/carro/vaciar")

def enviar_correo(**kwargs):
    
    asunto="Confirmación del pedido"
    mensaje=render_to_string('emails/pedido.html', {
        'pedido': kwargs.get('pedido'),
        'lineas_pedido':kwargs.get('lineas_pedido'),
        'nombre_usuario':kwargs.get('nombre_usuario'),
        'email_usuario':kwargs.get('email_usuario')
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email='albert23199@gmail.com'
    send_to=kwargs.get('email_usuario')
    
    send_mail(asunto, mensaje_texto, from_email, [send_to], html_message=mensaje)
    