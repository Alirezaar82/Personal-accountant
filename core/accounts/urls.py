from django.urls import path
from rest_framework_nested.routers import DefaultRouter

from .views import UserProfileViewSet,UserProfileChangeViewSet,CustomUserCreateView

urlpatterns = [
    path('account/auth/users/', CustomUserCreateView.as_view({'post': 'create'}), name='user-register'),
    path('profile/', UserProfileViewSet.as_view({'get': 'list'}),name='profile'),
    path('profile/change/', UserProfileChangeViewSet.as_view({'patch': 'partial_update', 'put': 'update', 'delete': 'destroy'}),name='profile-change'),
]