from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
