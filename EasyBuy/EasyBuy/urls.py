from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/users/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('api/sales/', include('sales.urls')),
]
