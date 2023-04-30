from django.db import models
from django.contrib.auth import get_user_model
from comprar.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

User=get_user_model()

class Pedido(models.Model):
    
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set-aggregate(
            
            total=Sum(F('precio')*F('cantidad'), output_field=FloatField)
        )['total']
    
    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad}x {self.producto.titulo}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name='Linea Pedido'
        verbose_name_plural='Lineas Pedidos'
        ordering=['id']
        
