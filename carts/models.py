from django.db import models


class Cart(models.Model):
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )


class CartProduct(models.Model):
    total_itens = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    
    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name="products",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="cart",
    )
