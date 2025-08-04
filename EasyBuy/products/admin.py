from django.contrib import admin
from .models import Product, ProductCategory, Brand, ProductSubCategory, ProductDepartment, ProductVariant
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(ProductDepartment)
admin.site.register(Brand)
admin.site.register(ProductVariant)