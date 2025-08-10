from rest_framework import viewsets, permissions
from .serializers import BrandSerializer, ProductCategorySerializer, ProductDepartmentSerializer, ProductSerializer, ProductSubCategorySerializer, ProductVariantSerializer
from .models import Product, Brand, ProductDepartment, ProductCategory, ProductSubCategory, ProductVariant

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer 

class ProductDepartmentViewSet(viewsets.ModelViewSet):
    queryset = ProductDepartment.objects.all()
    serializer_class = ProductDepartmentSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer