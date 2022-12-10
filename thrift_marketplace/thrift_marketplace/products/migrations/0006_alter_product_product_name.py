# Generated by Django 4.1.4 on 2022-12-10 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                validators=[django.core.validators.MinLengthValidator(2)],
                verbose_name="Product Name",
            ),
        ),
    ]