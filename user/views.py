from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CustomUser
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated(),)

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return (AllowAny(),)
        return self.permission_classes

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = serializer.save()
        except IntegrityError:
            return Response({"error": "user_id or username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        data = UserSerializer(user).data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')

        user = authenticate(request, user_id=user_id, password=password)
        if user:
            login(request, user)

            data = self.get_serializer(user).data
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return Response(data, status=status.HTTP_200_OK)

        return Response({"error": "Wrong username or wrong password"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['DELETE'])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        data = self.get_queryset()
        response = UserSerializer(data, many=True).data

        return Response(response, status=status.HTTP_200_OK)
