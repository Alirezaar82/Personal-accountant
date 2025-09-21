from rest_framework import viewsets,APIView
from rest_framework.permissions import IsAuthenticated

from .models import ExpenseCategoryModel, ExpenseModel, ExpenseLimitModel
from .serializers import (
    ExpenseCategorySerializer,
    CreateExpenseCategorySerializer,
    UpdateExpenseCategorySerializer,
    ExpenseSerializer,
    CreateExpenseSerializer,
    UpdateExpenseSerializer,
    ExpenseLimitSerializer,
    CreateExpenseLimitSerializer,
    UpdateExpenseLimitSerializer,
)

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return ExpenseCategoryModel.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateExpenseCategorySerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateExpenseCategorySerializer
        return ExpenseCategorySerializer
    
    def destroy(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            return Response({
                "status":"Notok",
                "detail": "You do not have permission to perform this action."
            },
            status=403,
        )
        return super().destroy(request, *args, **kwargs)

    
class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        category__pk = self.kwargs.get('category_pk')
        queryset =  ExpenseModel.objects.filter(user=self.request.user,category__pk=category__pk)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateExpenseSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateExpenseSerializer
        return ExpenseSerializer
    
    def destroy(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            return Response({
                "status":"Notok",
                "detail": "You do not have permission to perform this action."
            },
            status=403,
        )        
        return super().destroy(request, *args, **kwargs)


class ExpenseLimitViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseLimitSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return ExpenseLimitModel.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateExpenseLimitSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateExpenseLimitSerializer
        return ExpenseLimitSerializer

    def destroy(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            return Response({
                "status":"Notok",
                "detail": "You do not have permission to perform this action."
            },
            status=403,
        )
        return super().destroy(request, *args, **kwargs)

