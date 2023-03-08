from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from categories.models import Category
from users.permissions import SalesmanPermission
from .models import Product
from .serializer import ProductSerializer


class ProductView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        category_id = self.request.data.pop("category")
        category = get_object_or_404(Category, pk=category_id)
        return serializer.save(owner=self.request.user, category=category)
