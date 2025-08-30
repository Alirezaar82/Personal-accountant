from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from accounts.validators import validate_iranian_cellphone_number

class UserType(models.IntegerChoices):
    user = 1, _("user")
    superuser = 2, _("superuser")
    admin = 3, _("admin")


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not phone_number:
            raise ValueError(_("The Email must be set"))

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.superuser.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_('Phone Number'),max_length=15, validators=[validate_iranian_cellphone_number],unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    type = models.IntegerField(
        choices=UserType.choices, default=UserType.user.value)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number
    
    def get_fullname(self):
            if hasattr(self, 'user_profile'):
                return self.user_profile.get_fullname()
            return self.phone_number


class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE,related_name="user_profile")
    email = models.EmailField(blank=True,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile/",default="profile/default.png")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_fullname(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return _('new user')

# class SubscriptionPlanel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     duration_days = models.IntegerField()

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Subscription Plan'
#         verbose_name_plural = 'Subscription Plans'


# class SubscriptionModel(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')
#     plan = models.ForeignKey(SubscriptionPlanel, on_delete=models.CASCADE, related_name='subscriptions')
#     is_active = models.BooleanField(default=True)
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField()

#     def __str__(self):
#         return f"{self.user.phone_number} - {self.plan}"

#     class Meta:
#         verbose_name = 'Subscription'
#         verbose_name_plural = 'Subscriptions'

@receiver(post_save,sender=CustomUser)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance, pk=instance.pk)