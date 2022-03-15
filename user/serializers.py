from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    username = serializers.CharField()
    introduction = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            'user_id',
            'username',
            'introduction',
        )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        return user
