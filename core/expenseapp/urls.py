from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import ExpenseCategoryViewSet, ExpenseViewSet, ExpenseLimitViewSet

router = DefaultRouter()
router.register(r'expense-categories', ExpenseCategoryViewSet, basename='expense-categories')
router.register(r'expense-limits', ExpenseLimitViewSet, basename='expense-limits')
expense_categories_router = NestedDefaultRouter(router, r'expense-categories', lookup='category')
expense_categories_router.register(r'expenses', ExpenseViewSet, basename='category-expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(expense_categories_router.urls)),
]
