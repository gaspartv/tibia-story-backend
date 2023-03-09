from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from orders.models import Order
from carts.models import CartProduct
from orders.serializer import OrderSerializer
from products.models import Product


class OrderViewl(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            cart_id = self.request.user.cart.id
            products_cart = CartProduct.objects.all().filter(
                cart_id=cart_id, status=True
            )

            if products_cart.count() == 0:
                raise ValueError("O carrinho está vazio")

            price_total = 0
            products_list = []
            for product in products_cart:
                product_get = get_object_or_404(Product, id=product.product.id)
                price_total += product_get.price * product.total_itens
                products_list.append(
                    {
                        "id": product_get.id,
                        "name": product_get.name,
                        "description": product_get.description,
                        "price": str(product_get.price * product.total_itens),
                        "count": product.total_itens,
                    }
                )
                product.status = False
                product.save()

            Order.objects.create(
                total_order=price_total,
                user=self.request.user,
                products_list=products_list,
            )

            return Response(
                {
                    "Order": {
                        "Total": price_total,
                        "Products": products_list,
                    },
                },
                status.HTTP_201_CREATED,
            )
        except ValueError as e:
            return Response(
                {"Error": str(e)},
                status.HTTP_400_BAD_REQUEST,
            )
