"""wormgate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wormgateWeb import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wormgateWeb.urls')),
    path('comprar/', include('comprar.urls')),
    path('carro/', include('carro.urls')),
    path('contacto/', include('Contacto.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('autor/', include('autor.urls')),
    path('pedidos/', include('pedidos.urls')),
    
    
]
