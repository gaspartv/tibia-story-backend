from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from carts.models import Cart
from .permissions import IsUserPermission
from .models import User
from .serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        cart = Cart.objects.create()
        return serializer.save(cart=cart)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
