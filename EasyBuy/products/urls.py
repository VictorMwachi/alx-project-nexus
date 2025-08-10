from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', views.ProductViewSet)
router.register(r'variants', views.ProductVariantViewSet)
router.register(r'brands', views.BrandViewSet) 
router.register(r'departments', views.ProductDepartmentViewSet)
router.register(r'categories', views.ProductCategoryViewSet)
router.register(r'subcategories', views.ProductSubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]