from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet

# Create a router and register our viewset with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'/?', ClientViewSet, basename='client')

urlpatterns = [
]+router.urls
