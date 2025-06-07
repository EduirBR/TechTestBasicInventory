from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ProductModel, InventoryModel
from .serializers import ProductSerializer, InventorySerializer

