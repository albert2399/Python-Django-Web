from django.contrib import admin
from .models import LineaPedido, Pedido

# Register your models here.

admin.site.register(Pedido)
admin.site.register(LineaPedido)

