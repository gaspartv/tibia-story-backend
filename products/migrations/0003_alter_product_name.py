# Generated by Django 4.1.7 on 2023-03-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_productscategories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
