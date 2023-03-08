from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    cart = models.OneToOneField(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name="cart_user",
        null=True
    )
