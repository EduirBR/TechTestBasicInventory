from django.urls import path

from .views import index, login, register, dashboard, logout, clients, products, inventory

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('clients', clients, name='clients'),
    path('products', products, name='products'),
    path('inventory', inventory, name='inventory'),
]
