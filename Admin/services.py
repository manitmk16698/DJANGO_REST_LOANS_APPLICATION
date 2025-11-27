from Admin.models import AdminFinancialInstitution, BankProduct, Category,Product
from django.shortcuts import get_object_or_404

class FinancialInstitutionService:

    @staticmethod
    def list_all():
        return AdminFinancialInstitution.objects.all().order_by('-Financial_institution_id')

    @staticmethod
    def create(validated_data):
        return AdminFinancialInstitution.objects.create(**validated_data)

    @staticmethod
    def get_by_id(inst_id):
        return get_object_or_404(AdminFinancialInstitution, Financial_institution_id=inst_id)

    @staticmethod
    def update(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
        return True


class ProductService:

    @staticmethod
    def list_all():
        return Product.objects.all().order_by('-created_at')

    @staticmethod
    def create(validated_data):
        return Product.objects.create(**validated_data)

    @staticmethod
    def get_by_id(product_id):
        return get_object_or_404(Product, product_id=product_id)

    @staticmethod
    def update(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
        return True
    



class CategoryService:

    @staticmethod
    def list_all():
        return Category.objects.all().order_by('-created_at')

    @staticmethod
    def create(validated_data):
        return Category.objects.create(**validated_data)

    @staticmethod
    def get_by_id(category_id):
        return get_object_or_404(Category, category_id=category_id)

    @staticmethod
    def update(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
        return True
    

class BankProductService:

    @staticmethod
    def list_all():
        return BankProduct.objects.all().order_by('-created_at')

    @staticmethod
    def create(validated_data):
        return BankProduct.objects.create(**validated_data)

    @staticmethod
    def get_by_id(bank_product_id):
        return get_object_or_404(BankProduct, bank_product_id=bank_product_id)

    @staticmethod
    def update(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
        return True