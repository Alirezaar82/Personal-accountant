from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        fields = ['id','phone_number']



class UserCreateSerializer(DjoserUserCreateSerializer):
    phone_number = serializers.CharField(required=True)
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = ['id', 'phone_number', 'password']

# class UserCreateSerializer(DjoserUserCreateSerializer):
#     phone_number = serializers.CharField(required=True)  # فیلد شماره تلفن

#     class Meta(DjoserUserCreateSerializer.Meta):
#         model = User
#         fields = ['id', 'phone_number', 'password']

#     def create(self, validated_data):
#         # ایجاد کاربر جدید
#         user = super().create(validated_data)
        
#         # ساخت توکن JWT
#         refresh = RefreshToken.for_user(user)
        
#         # افزودن توکن‌ها به داده‌های پاسخ
#         self._tokens = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
        
#         return user

#     def to_representation(self, instance):
#         # بازگشت اطلاعات کاربر به همراه توکن‌ها
#         rep = super().to_representation(instance)
#         rep['refresh'] = self._tokens['refresh']
#         rep['access'] = self._tokens['access']
#         return rep




class UserProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['phone_number','user_type','email','full_name','last_login']

    def get_phone_number(self, profile):
        return profile.user.phone_number
    
    def get_user_type(self, profile):
        return profile.user.get_user_type()['label']

    def get_last_login(self, profile):
        return profile.user.last_login

    
class UserProfileChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['email', 'full_name',]
    