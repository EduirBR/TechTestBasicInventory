from uuid import uuid4
from django.db import models


class ProductModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'products'


class InventoryModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    stock_quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    observations = models.TextField(blank=True, null=True)
    fk_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'inventory'

