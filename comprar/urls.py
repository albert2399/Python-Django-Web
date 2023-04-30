from django.urls import path
from comprar import views

urlpatterns = [
    
    path('', views.comprar, name='Comprar'),

]
