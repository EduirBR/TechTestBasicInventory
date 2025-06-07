from rest_framework import serializers

from .models import ProductModel, InventoryModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    
    fk_product = ProductSerializer()
    
    class Meta:
        model = InventoryModel
        fields = '__all__'

