# Generated by Django 4.1.4 on 2022-12-10 14:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo_picture",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="Photo"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="products.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
