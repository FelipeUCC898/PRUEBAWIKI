from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class personal_Information(models.Model):
    names = models.CharField(max_length=100, verbose_name="Nombres")
    last_names = models.CharField(max_length=100, verbose_name="Apellidos")
    position = models.CharField(max_length=100, verbose_name="cargo")
    date = models.DateField(null=True, blank=True, verbose_name=("fecha"))
    description = models.CharField(max_length=100, verbose_name="descripción")
    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name=("fecha"))
    update_at = models.DateField(auto_now=True, null=True, blank=True, verbose_name=("fecha"))

    class Meta: 
        verbose_name = 'Informacion Personal'
        verbose_name_plural = 'Informaciones Personales'
    
    def __str__(self):
        return str(self.names)