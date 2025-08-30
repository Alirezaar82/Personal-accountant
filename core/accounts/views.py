from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from djoser.views import UserViewSet

from .serializers import UserProfileSerializer,UserProfileChangeSerializer
from .models import Profile


class CustomUserCreateView(UserViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data,
        }, status=status.HTTP_201_CREATED)


class UserProfileViewSet(ModelViewSet):
    http_method_names = ['get','put', 'delete','head','options']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class UserProfileChangeViewSet(ModelViewSet):
    http_method_names = [ 'patch','put', 'delete','head','options']
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        return UserProfileChangeSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)