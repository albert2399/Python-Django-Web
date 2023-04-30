from django.urls import path
from Contacto import views


urlpatterns = [
    
    path('', views.contacto, name='Contacto'),
    
]
