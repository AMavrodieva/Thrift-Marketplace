# Generated by Django 4.1.4 on 2022-12-10 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_product_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                blank=True,
                max_length=35,
                null=True,
                validators=[django.core.validators.MinLengthValidator(2)],
                verbose_name="Product Name",
            ),
        ),
    ]
