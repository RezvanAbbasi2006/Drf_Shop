from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.home.serializers import HomeSerializer
from apps.product.models import Product, ProductCategory


class Home(APIView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.order_by("-created_at")
        category = ProductCategory.objects.all()
        data = {
            "product": products,
            "category": category
        }

        serializer = HomeSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)
