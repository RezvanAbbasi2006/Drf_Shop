from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.carts.models import Cart, CartItem, Transaction
from apps.product.models import Product
from apps.carts.serilizers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    Cart Api
    """
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get carts by item or items
        """
        cart = Cart.objects.get_or_create(
            owner_id=self.request.user.id
        )
        return cart

    def list(self, request, *args, **kwargs):
        """
        Show details of spacial carts
        """
        cart = self.get_queryset()
        serializer = self.serializer_class(cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Create new carts or get exist carts and add selected items for user how logged in
        """
        product_id = request.data['product_id']
        product_count = request.data['count']

        product = Product.objects.get(id=product_id)

        cart = self.get_queryset()

        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_item_exist = Cart.objects.filter(
            carts__product_id=product_id,
            owner_id=request.user.id
        ).first()

        if cart_item_exist:
            cart_item_exist.count += product_count
            cart_item_exist.save()
            return Response(status=status.HTTP_200_OK)

        cart_item = CartItem.objects.create(
            is_ordered=True,
            count=product_count,
            product=product
        )

        transaction = Transaction.objects.create(
            customer=request.user
        )

        return Response(status=status.HTTP_201_CREATED)
