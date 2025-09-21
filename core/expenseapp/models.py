from django.db import models

class ExpenseCategoryModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategoryModel, on_delete=models.CASCADE)
    totoal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseLimitModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

