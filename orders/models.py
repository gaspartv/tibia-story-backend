from django.db import models


class OrderStatusChoices(models.TextChoices):
    IN_PROGRESS = "in progress"
    CONCLUDED = "concluded"


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.IN_PROGRESS,
    )
    total_order = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    products_list = models.JSONField(default=dict)
