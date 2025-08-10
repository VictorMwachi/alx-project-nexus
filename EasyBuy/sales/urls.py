from django.urls import path
from .views import WishlistView, CartView, OrderView, OrderItemView
urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/', OrderView.as_view(), name='order'),
    path('order-item/', OrderItemView.as_view(), name='order-item'),
]