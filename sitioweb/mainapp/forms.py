from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'}))
    email=forms.CharField(label='Correo electrónico', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electronico'}))
    first_name=forms.CharField(label='Nombres', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombres'}))
    last_name=forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}))
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    password2=forms.CharField(label='Verifica tu contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Verifica tu contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class PersonalForm(forms.ModelForm):
    names=forms.CharField(label='nombres', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombres'}))
    last_names=forms.CharField(label='apellidos', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'apellidos'}))
    position=forms.CharField(label='que cargo ejerce', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'que cargo ejerce'}))

    class Meta:
        model = User
        fields = ("names","last_names", "position")
