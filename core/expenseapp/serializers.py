from rest_framework import serializers

from .models import ExpenseCategoryModel, ExpenseModel, ExpenseLimitModel

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategoryModel
        fields = '__all__' 
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')


class CreateExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategoryModel
        fields = ('category_name', 'description', 'limit_amount')
    
    def create(self, validated_data):
        user = self.context['request'].user
        return ExpenseCategoryModel.objects.create(
            user=user,
            **validated_data
        )


class UpdateExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategoryModel
        fields = ('category_name', 'description', 'limit_amount')
    
    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.description = validated_data.get('description', instance.description)
        instance.limit_amount = validated_data.get('limit_amount', instance.limit_amount)
        instance.save()
        return instance


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = '__all__' 
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')   


class CreateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ('category', 'totoal_amount', 'description', 'date')
    
    def create(self, validated_data):
        user = self.context['request'].user
        return ExpenseModel.objects.create(
            user=user,
            **validated_data
        )


class UpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ('category', 'totoal_amount', 'description', 'date')
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.totoal_amount = validated_data.get('totoal_amount', instance.totoal_amount)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class ExpenseLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseLimitModel
        fields = '__all__' 
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')   


class CreateExpenseLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseLimitModel
        fields = ('limit_amount',)
    
    def create(self, validated_data):
        user = self.context['request'].user
        return ExpenseLimitModel.objects.create(
            user=user,
            **validated_data
        )


class UpdateExpenseLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseLimitModel
        fields = ('limit_amount',)
    
    def update(self, instance, validated_data):
        instance.limit_amount = validated_data.get('limit_amount', instance.limit_amount)
        instance.save()
        return instance

