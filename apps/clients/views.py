from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import ClientModel
from .serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    """
    ViewSet for managing clients.
    """
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        print("Retrieving client data")
        return super().retrieve(request, *args, **kwargs)
