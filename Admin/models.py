from django.db import models
import uuid

class AdminFinancialInstitution(models.Model):
    Financial_institution_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
    bank = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    dsa_code = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'admin_financial_institution'  # Custom table name
        verbose_name = 'Financial Institution'
        verbose_name_plural = 'Financial Institutions'

    def __str__(self):
        return self.bank


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name



class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    


class BankProduct(models.Model):
    bank_product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    bank = models.ForeignKey(
        AdminFinancialInstitution,
        on_delete=models.CASCADE,
        related_name="bank_products"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="bank_products"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bank_product_junction"
        unique_together = ('bank', 'product')   # prevents duplicates

    def __str__(self):
        return f"{self.bank.bank} → {self.product.product_name}"