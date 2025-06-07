from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator

class ClientModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='Phone number must contain only digits',
                code='invalid_phone_number'
            )
        ]
    )
    address = models.TextField()

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.name
