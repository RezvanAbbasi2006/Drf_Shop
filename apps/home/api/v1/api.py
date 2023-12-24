from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.home.serializers import HomeSerializer
from apps.product.models import Product, ProductCategory


class Home(APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        # category = ProductCategory.objects.all()

        data = {
            "products": product,
            # "category": category
        }
        serializer = HomeSerializer(data=data)
        print("DATA   :", data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
