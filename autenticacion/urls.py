from django.urls import path
from .views import  log_out, logear, crear_usuario
# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    
    path('', crear_usuario, name='registro'),
    
    path('logout/', log_out, name='logout'),
    
    path('login/', logear, name='login'),

# urlpatterns = [
#     path('register/', CreateView.as_view(
#             template_name='autenticacion.html',
#             form_class=UserCreationForm,
#             success_url='/'))
#     ]
    
]
