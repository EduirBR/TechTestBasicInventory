from django.shortcuts import render, redirect
from django.contrib import messages



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

