from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import IncomeCategoryViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'Income-categories', IncomeCategoryViewSet, basename='Income-categories')
Income_categories_router = NestedDefaultRouter(router, r'Income-categories', lookup='category')
Income_categories_router.register(r'Incomes', IncomeViewSet, basename='category-Incomes')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(Income_categories_router.urls)),
]
