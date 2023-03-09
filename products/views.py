from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from categories.models import Category
from carts.models import CartProduct, Cart
from users.permissions import SalesmanPermission
from .models import Product
from .serializer import ProductSerializer, ProductBuySerializer
import ipdb


class ProductView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        category_id = self.request.data.pop("category")
        category = get_object_or_404(Category, pk=category_id)
        return serializer.save(owner=self.request.user, category=category)


class ProductBuyView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CartProduct.objects.all()
    serializer_class = ProductBuySerializer

    def perform_create(self, serializer):
        cart = self.request.user.cart
        product_id = self.kwargs.get("pk")
        product = get_object_or_404(Product, id=product_id)

        if "total_itens" in self.request.data:
            total_itens = self.request.data["total_itens"]
        else:
            total_itens = 1

        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=product,
            status=True,
        ).first()
        if cart_product:
            cart_product.total_itens += total_itens
            cart_product.total_price += total_itens * product.price
            cart_product.save()
            return cart_product
        else:
            return serializer.save(
                cart=cart,
                product=product,
                total_itens=total_itens,
                total_price=total_itens * product.price,
            )


class ProductBuyListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductBuySerializer

    def get_queryset(self):
        cart = CartProduct.objects.filter(
            cart=self.request.user.cart,
            status=True,
        )
        return cart
