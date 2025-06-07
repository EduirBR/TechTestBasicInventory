from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register our viewset with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'/?', ProductViewSet, basename='product')

urlpatterns = router.urls
