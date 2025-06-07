from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404

from .models import ProductModel, InventoryModel
from .serializers import ProductSerializer, InventoryWithProductSerializer


class ProductViewSet(ModelViewSet):
    """
    ViewSet for managing products.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Crea un producto y su inventario inicial"""
        product = serializer.save()
        # Crear registro de inventario con stock inicial en 0
        InventoryModel.objects.create(
            fk_product=product,
            stock_quantity=0,
            observations="Inventario inicial"
        )
        return product

    def destroy(self, request, *args, **kwargs):
        """
        Impide eliminar productos que tienen stock mayor a 0
        """
        product = self.get_object()
        inventory = InventoryModel.objects.filter(fk_product=product).first()
        
        if inventory and inventory.stock_quantity > 0:
            return Response(
                {"error": "No se puede eliminar un producto con stock disponible"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().destroy(request, *args, **kwargs)


class InventoryViewSet(ReadOnlyModelViewSet, UpdateModelMixin):
    """
    ViewSet for managing inventory.
    """
    queryset = InventoryModel.objects.select_related('fk_product').all()
    serializer_class = InventoryWithProductSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = InventoryWithProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InventoryModel.objects.select_related('fk_product').all()

