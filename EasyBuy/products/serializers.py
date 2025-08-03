from rest_framework import serializers
from .models import Brand,Product, ProductCategory, ProductSubCategory ,ProductDepartment#, ProductImage

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDepartment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = '__all__'