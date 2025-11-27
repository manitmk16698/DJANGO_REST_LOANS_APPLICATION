# from django.urls import path

# urlpatterns=[
#     path()
# ]
# 
from django.urls import path
from Admin.views import (
    BankProductListCreateAPIView,
    BankProductRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    FinancialInstitutionListCreateAPIView,
    FinancialInstitutionRetrieveUpdateDestroyAPIView,ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('financial-institutions/', FinancialInstitutionListCreateAPIView.as_view(),name='financial-institution-list-create'),
    path('financial-institutions/<uuid:pk>/', FinancialInstitutionRetrieveUpdateDestroyAPIView.as_view(),name='financial-institution-detail'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('bank-products/', BankProductListCreateAPIView.as_view(), name='bank-product-list-create'),
    path('bank-products/<uuid:pk>/', BankProductRetrieveUpdateDestroyAPIView.as_view(), name='bank-product-detail'),
]
