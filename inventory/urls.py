
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from jwt_custom.views import ValidateTokenView


urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin', admin.site.urls),
    path('api', include('apps.users.urls')),
    path('api/clients', include('apps.clients.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify', ValidateTokenView.as_view(), name='token_verify'),
]
