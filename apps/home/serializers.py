from rest_framework import serializers

from apps.home.models import Home
from apps.product.serilizers import ProductSerializer, ProductCategorySerializer


class HomeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    category = ProductCategorySerializer(many=True)

