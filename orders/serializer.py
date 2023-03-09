from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products_list = serializers.JSONField()

    def create(self, validated_data: dict):
        return Order.objects.create(**validated_data)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "total_order",
            "ordered_at",
            "user",
            "products_list",
        ]
        read_only_fields = [
            "user",
            "ordered_at",
            "total_order",
            "products_list",
        ]
