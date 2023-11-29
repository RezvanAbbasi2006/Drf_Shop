from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.models.cart.models import Cart, CartItem
from apps.models.product.models import Product
from apps.serilizers.cart.serilizers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = Cart.objects.prefetch_related("cart_item").get_or_create(
            customer_id=self.request.user.id)
        return cart

    def list(self, request, *args, **kwargs):
        cart = self.get_queryset()
        serializer = self.serializer_class(cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        cart = self.get_queryset()
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        product_count = serializer.validated_data['count']

        product_exist = Cart.cart_item.filter(
            product=product,
            user_id=request.user.id
        ).first()
        if product_exist:
            product_exist.count += product_count
            product_exist.save()
            return Response(status=status.HTTP_200_OK)

        CartItem.objects.create(
            cart_id=cart.id,
            product=product,
            count=product_count
        )
        return Response(status=status.HTTP_201_CREATED)
