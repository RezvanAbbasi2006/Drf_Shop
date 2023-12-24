from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.serilizers import ProductSerializer, ProductCategorySerializer


class ProductAPI(APIView):

    def get(self, request, format=None):
        query_set = Product.objects.all()

        return Response(
            {"data": ProductSerializer(query_set, many=True).data},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class ProductCategoryAPI(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
