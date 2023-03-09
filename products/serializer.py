from rest_framework import serializers
from carts.models import CartProduct
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "storage",
            "price",
            "description",
            "image",
            "category",
            "owner",
        ]
        read_only_fields = ["owner"]


class ProductBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = [
            "id",
            "total_itens",
            "total_price",
            "cart",
            "product",
            "status",
        ]
        read_only_fields = ["cart", "product", "status"]
