from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.models.product.models import Product
from apps.serilizers.product.serilizers import ProductSerializer


class ProductAPI(APIView):
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        query_set = Product.objects.all()

        return Response(
            {"data": self.serializer_class(query_set, many=True).data},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )