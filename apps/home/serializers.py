from rest_framework import serializers

from apps.home.models import Home
from apps.product.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class HomeSerializer(serializers.Serializer):
    product = ProductSerializer(many=True)
    category = ProductCategorySerializer(many=True)
