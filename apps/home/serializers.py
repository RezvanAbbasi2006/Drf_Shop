from rest_framework import serializers

from apps.home.models import Home
from apps.product.serilizers import ProductSerializer, ProductCategorySerializer


class HomeSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    category = ProductCategorySerializer

    class Meta:
        model = Home
        fields = '__all__'
