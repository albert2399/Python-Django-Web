from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from .forms import Registro


# Create your views here.

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']


# class Registro(View):
    
   
    # def get(self, request):
    #     form=UserCreationForm()
    #     return render(request, 'autenticacion.html', {'form':form})
    
    # def post(self, request):
    #     form=UserCreationForm(request.POST)
        
    #     if form.is_valid():
        
    #         usuario=form.save()
        
    #         login(request, usuario)
        
    #         return redirect('Home')
        
    #     else:
    #         for msg in form.error_messages:
    #             messages.error(request, form.error_messages[msg])
                
    #         return render(request, 'autenticacion.html',{'form':form})

def crear_usuario(request):
    form = Registro()
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')
    else:
        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])

    return render(request, 'autenticacion.html', {'form': form})
        
        
def log_out(request):
    
    logout(request)
    
    return redirect('Home')

def logear(request):
    
    if request.method == 'POST':
        
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, 'usuario o contraseña incorrecto')
                
        else:
            messages.error(request, 'usuario o contraseña incorrecto')
        
    
    form=AuthenticationForm()
    
    return render(request, 'login.html',{'form':form})

# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True,
#                          label='Email',
#                          error_messages={'exists': 'Oops'})

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")


#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

#     def clean_email(self):
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise ValidationError(self.fields['email'].error_messages['exists'])
#         return self.cleaned_data['email']