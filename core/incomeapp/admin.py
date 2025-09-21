from django.contrib import admin

from django.contrib import admin

from .models import IncomeCategoryModel, IncomeModel


@admin.register(IncomeCategoryModel)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category_name', 'limit_amount', 'created_at', 'updated_at')
    search_fields = ('category_name', 'user__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(IncomeModel)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'totoal_amount', 'date', 'created_at', 'updated_at')
    search_fields = ('category__category_name', 'user__username')
    list_filter = ('date', 'created_at', 'updated_at')
    ordering = ('-created_at',)

