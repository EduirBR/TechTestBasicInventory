from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from apps.products.models import ProductModel, InventoryModel
from apps.clients.models import ClientModel

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Obtener número total de productos únicos
            total_products = ProductModel.objects.count()

            # Obtener la suma total de items en inventario
            total_inventory = InventoryModel.objects.aggregate(
                total_stock=Sum('stock_quantity')
            )['total_stock'] or 0

            # Obtener número total de clientes
            total_clients = ClientModel.objects.count()

            return Response({
                'total_products': total_products,
                'total_inventory': total_inventory,
                'total_clients': total_clients
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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

def products(request):
    """
    Vista para mostrar la lista de productos.
    """
    return render(request, 'products.html')

def inventory(request):
    return render(request, 'inventory.html')

