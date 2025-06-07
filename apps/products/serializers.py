from rest_framework import serializers
from .models import ProductModel, InventoryModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'price', 'category']


class InventoryWithProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='fk_product.name', read_only=True)
    
    class Meta:
        model = InventoryModel
        fields = ['id', 'product_name', 'stock_quantity', 'observations', 'last_updated', 'fk_product']

