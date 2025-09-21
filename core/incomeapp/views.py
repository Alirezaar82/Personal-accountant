from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import IncomeCategoryModel,IncomeModel
from .serializers import (
    IncomeCategorySerializer,
    CreateIncomeCategorySerializer,
    UpdateIncomeCategorySerializer,
    IncomeSerializer,
    CreateIncomeSerializer,
    UpdateIncomeSerializer
)


class IncomeCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return IncomeCategoryModel.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateIncomeCategorySerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateIncomeCategorySerializer
        return IncomeCategorySerializer
    
    def destroy(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            return Response({
                "status":"Notok",
                "detail": "You do not have permission to perform this action."
            },
            status=403,
        )
        return super().destroy(request, *args, **kwargs)

    
class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        category__pk = self.kwargs.get('category_pk')
        queryset =  IncomeModel.objects.filter(user=self.request.user,category__pk=category__pk)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateIncomeSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateIncomeSerializer
        return IncomeSerializer
    
    def destroy(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            return Response({
                "status":"Notok",
                "detail": "You do not have permission to perform this action."
            },
            status=403,
        )        
        return super().destroy(request, *args, **kwargs)
