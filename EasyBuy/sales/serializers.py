from rest_framework import serializers
from .models import Wishlist, Cart, Order, OrderItem
from products.serializers import ProductSerializer, ProductVariantSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_variant = ProductVariantSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'product', 'product_variant', 'created_at']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_variant = ProductVariantSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'product_variant', 'quantity', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'order_uuid', 'user', 'total_price', 'shipping_fee', 'voucher_discount', 'shipping_discount', 'payment_method', 'payment_status', 'created_at', 'items']

    def get_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_variant = ProductVariantSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_variant', 'quantity', 'price']