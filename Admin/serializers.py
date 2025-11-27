from rest_framework import serializers
from Admin.models import AdminFinancialInstitution, BankProduct, Category,Product

class AdminFinancialInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminFinancialInstitution
        fields = [
            'Financial_institution_id',
            'bank',
            'short_name',
            'dsa_code',
            'pincode',
            'logo',
            'location'
        ]




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_name',
            'created_at',
            'updated_at'
        ]




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_id',
            'category_name',
            'created_at',
            'updated_at'
        ]

class BankProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProduct
        fields = [
            'bank_product_id',
            'bank',
            'product',
            'is_active',
            'created_at',
            'updated_at'
        ]