# Generated by Django 4.1.7 on 2023-03-08 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_remove_category_product"),
        ("products", "0003_alter_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="categories.category",
            ),
        ),
        migrations.DeleteModel(
            name="ProductsCategories",
        ),
    ]