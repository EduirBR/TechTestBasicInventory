from rest_framework import serializers
from .models import ClientModel

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
