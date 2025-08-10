from django.urls import path
from .views import WishlistView, CartView, OrderView, OrderItemView,AddToCartView, RemoveFromCartView, ClearCartView
urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/clear/', ClearCartView.as_view(), name='clear-cart'),
    path('order/', OrderView.as_view(), name='order'),
    path('order-item/', OrderItemView.as_view(), name='order-item'),
]