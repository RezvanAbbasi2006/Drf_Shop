from rest_framework import serializers

from apps.product.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

    def create(self, validated_data, *args, **kwargs):
        print("VALIDATED DATA    :", validated_data)
        title = validated_data['title']
        type = validated_data['type']
        description = validated_data['description']

        cat = ProductCategory(
            title=title,
            type=type,
            description=description
        )
        cat.save()
        return cat


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ModelSerializer(ProductCategorySerializer)

    class Meta:
        model = Product
        fields = "__all__"
