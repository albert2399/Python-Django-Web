from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Registro(UserCreationForm):
    
    email=forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']

# from .models import Usuario

# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['username', 'email', 'password']