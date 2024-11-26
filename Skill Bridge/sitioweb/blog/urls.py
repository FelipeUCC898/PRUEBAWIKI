from django.urls import path
from .views import publicacion, create_article

urlpatterns = [
    path('publicacion', publicacion, name='publicacion'),
    path('crearPublicacion', create_article, name='crearPublicacion'),
    
]
 