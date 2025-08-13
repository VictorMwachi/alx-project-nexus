from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wishlist, Cart, Order, OrderItem
from products.models import Product, ProductVariant
from .serializers import WishlistSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from users.permissions import IsBuyerUser

# Create your views here.
class WishlistView(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerUser]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBuyerUser]

    def post(self, request):
        product_id = request.data.get("product")
        product_variant_id = request.data.get("product_variant")
        quantity = int(request.data.get("quantity", 1))

        product = Product.objects.get(id=product_id)
        product_variant = ProductVariant.objects.get(id=product_variant_id) if product_variant_id else None
        cart, created = Cart.objects.get_or_create(user=request.user,product=product, product_variant=product_variant)
        
        if not created:
            cart.quantity += quantity
        else:
            cart.quantity = quantity
        cart.save()

        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBuyerUser]

    def delete(self, request, item_id):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({"error": "No active cart"}, status=status.HTTP_404_NOT_FOUND)

        try:
            item = Cart.objects.get(id=item_id, cart=cart)
            item.delete()
        except Cart.DoesNotExist:
            return Response({"error": "Item not found in your cart"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Item removed"}, status=status.HTTP_200_OK)

class ClearCartView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBuyerUser]

    def delete(self, request, *args, **kwargs):
        """Clear all items from user's cart"""
        deleted_count = Cart.objects.filter(user=request.user).delete()[0]
        
        return Response({
            'message': f'Cart cleared successfully. {deleted_count} items removed.',
            'cart_summary': {
                'items': [],
                'total_amount': 0,
                'total_items': 0
            }
        })

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerUser]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderItemView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsBuyerUser]

    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)