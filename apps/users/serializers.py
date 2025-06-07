from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password',  'is_active' ]
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'is_active': {'read_only': True},
        }

    def create(self, validated_data):
        user: UserModel = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
