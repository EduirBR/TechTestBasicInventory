from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, InventoryViewSet

# Create a router and register our viewset with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'/?', ProductViewSet, basename='product')
router.register(r'/inventory/?', InventoryViewSet, basename='inventory')

urlpatterns = [
] + router.urls
