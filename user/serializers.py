from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    introduction = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            'user_id',
            'username',
            'password',
            'introduction',
        )

    def validate_password(self, value):
        return make_password(value)

    def validate(self, data):
        user_id = data.get('user_id')
        password = data.get('password')
        return data

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        Token.objects.create(user=user)
        return user
