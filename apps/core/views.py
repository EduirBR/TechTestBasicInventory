from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpRequest

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    """
    Vista para manejar el cierre de sesión.
    Redirige al login y muestra un mensaje de éxito.
    Los tokens se eliminan desde el frontend.
    """
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('login')


def clients(request):
    return render(request, 'clients.html')

