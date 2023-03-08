from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    storage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
    )
