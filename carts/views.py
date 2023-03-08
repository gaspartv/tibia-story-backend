from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import SalesmanPermission
from .models import Cart
from .serializer import CartSerializer


class CartView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]
    queryset = Cart.objects.all().order_by("id")
    serializer_class = CartSerializer
