from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManagerModel(BaseUserManager):
    def create_user(self, password, **extraField):
        user = self.model( **extraField)
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user
    def set_password(self,password):
        self.model.set_password(self,raw_password=password)
        self.model.save()
        return self

    def create_superuser(self, **extraField):
        user = self.create_user(**extraField)
        user.save()
        return user

class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4(), primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManagerModel()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    class Meta:
        db_table = 'users'
