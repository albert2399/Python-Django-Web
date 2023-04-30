from django.urls import path
from wormgateWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('personajes/', views.personajes, name='Personajes'),
    path('capitulo-1/', views.personajes, name='Primer Capítulo'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)