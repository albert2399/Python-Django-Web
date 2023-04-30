from inspect import formatannotation
from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo=models.CharField(max_length=32)
    formato=models.CharField(max_length=30)
    precio=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='comprar')
    fecha=models.DateField()
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
    def __str__(self):
        return self.titulo