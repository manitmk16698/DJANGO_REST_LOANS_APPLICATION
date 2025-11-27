from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from Admin.serializers import AdminFinancialInstitutionSerializer, BankProductSerializer, CategorySerializer, ProductSerializer
from Admin.services import BankProductService, CategoryService, FinancialInstitutionService, ProductService

class FinancialInstitutionListCreateAPIView(ListCreateAPIView):
    serializer_class = AdminFinancialInstitutionSerializer

    def get_queryset(self):
        return FinancialInstitutionService.list_all()

    def perform_create(self, serializer):
        FinancialInstitutionService.create(serializer.validated_data)

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from Admin.serializers import AdminFinancialInstitutionSerializer
from Admin.services import FinancialInstitutionService

class FinancialInstitutionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdminFinancialInstitutionSerializer

    def get_object(self):
        inst_id = self.kwargs.get("pk")
        return FinancialInstitutionService.get_by_id(inst_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        FinancialInstitutionService.update(instance, serializer.validated_data)

    def perform_destroy(self, instance):
        FinancialInstitutionService.delete(instance)



class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return ProductService.list_all()

    def perform_create(self, serializer):
        ProductService.create(serializer.validated_data)

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        product_id = self.kwargs.get("pk")
        return ProductService.get_by_id(product_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        ProductService.update(instance, serializer.validated_data)

    def perform_destroy(self, instance):
        ProductService.delete(instance)


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return CategoryService.list_all()

    def perform_create(self, serializer):
        CategoryService.create(serializer.validated_data)

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_object(self):
        category_id = self.kwargs.get("pk")
        return CategoryService.get_by_id(category_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        CategoryService.update(instance, serializer.validated_data)

    def perform_destroy(self, instance):
        CategoryService.delete(instance)


class BankProductListCreateAPIView(ListCreateAPIView):
    serializer_class = BankProductSerializer

    def get_queryset(self):
        return BankProductService.list_all()

    def perform_create(self, serializer):
        BankProductService.create(serializer.validated_data)

class BankProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BankProductSerializer

    def get_object(self):
        bank_product_id = self.kwargs.get("pk")
        return BankProductService.get_by_id(bank_product_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        BankProductService.update(instance, serializer.validated_data)

    def perform_destroy(self, instance):
        BankProductService.delete(instance)