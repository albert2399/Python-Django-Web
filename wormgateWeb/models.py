from django.db import models


class Personaje(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=530)
    imagen=models.ImageField(upload_to='comprar')
    
    class Meta:
        verbose_name='personaje'
        verbose_name_plural='personajes'
        
    def __str__(self):
        return self.nombre
    