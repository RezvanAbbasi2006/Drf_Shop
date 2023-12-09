from rest_framework import serializers

from apps.product.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ModelSerializer(ProductCategorySerializer)

    class Meta:
        model = Product
        fields = "__all__"
