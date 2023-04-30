from django.db import models

# Create your models here.

class Foto(models.Model):
    titulo=models.CharField(max_length=32)
    imagen=models.ImageField(upload_to='autor')
    
    class Meta:
        verbose_name='foto'
        verbose_name_plural='fotos'
        
    def __str__(self):
        return self.titulo
    