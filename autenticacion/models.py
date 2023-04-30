from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()