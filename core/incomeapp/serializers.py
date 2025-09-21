from rest_framework import serializers

from .models import IncomeCategoryModel,IncomeModel

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategoryModel
        fields = '__all__' 
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')


class CreateIncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategoryModel
        fields = ('category_name', 'description')
    
    def create(self, validated_data):
        user = self.context['request'].user
        return IncomeCategoryModel.objects.create(
            user=user,
            **validated_data
        )


class UpdateIncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategoryModel
        fields = ('category_name', 'description')
    
    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = '__all__' 
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')   


class CreateIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = ('category', 'totoal_amount', 'description', 'date')
    
    def create(self, validated_data):
        user = self.context['request'].user
        return IncomeModel.objects.create(
            user=user,
            **validated_data
        )


class UpdateIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = ('category', 'totoal_amount', 'description', 'date')
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.totoal_amount = validated_data.get('totoal_amount', instance.totoal_amount)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

