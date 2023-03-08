from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import SalesmanPermission
from .models import Category
from .serializer import CategorySerializer


class CategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
