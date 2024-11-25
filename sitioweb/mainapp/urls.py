from django.urls import path
from .views import index, login_page, logout_user, register, profile, social_network

urlpatterns = [
    path('', index, name='index'),
    path('inicio', index, name='index'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('social_network', social_network, name='social_network'),
]
 