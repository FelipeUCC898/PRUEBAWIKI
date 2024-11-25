from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'Home',
    })

def login_page(request):

    if request.user.is_authenticated:
        return redirect('publicacion')
    else:
        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('pass')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('publicacion')
            else:
                messages.warning(request, "Usuario o contraseña incorrectos")
    
    return render(request, 'mainapp/login.html',{
        'title': 'Login',
    })

def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_Form = RegisterForm()

        if request.method == 'POST':
            register_Form=RegisterForm(request.POST)

            if register_Form.is_valid():
                         
                register_Form.save()
                messages.success(request, "Se creo la cuenta")
                return redirect('login')

    return render(request, 'mainapp/register.html',{
        'title': 'Registro',
        'register_form':register_Form
    })

def profile(request):

    return render(request, 'mainapp/profile.html',{
        'title': 'Perfil',
    })

def social_network(request):

    return render(request, 'mainapp/social_network.html',{
        'title': 'social_ network',
    })