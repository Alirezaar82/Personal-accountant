from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """
    model = User
    list_display = ("id", "phone_number", "is_superuser", "is_active", "is_verified")
    list_filter = ("phone_number", "is_superuser", "is_active", "is_verified")
    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("phone_number", "password"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "Group Permissions",
            {
                "fields": ("groups", "user_permissions", "type"),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "type"
                ),
            },
        ),
    )

@admin.register(Profile)
class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "first_name", "last_name", 'email')
    search_fields = ("user__phone_number", "first_name", "last_name", 'email')
