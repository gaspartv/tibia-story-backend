from rest_framework import serializers
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
