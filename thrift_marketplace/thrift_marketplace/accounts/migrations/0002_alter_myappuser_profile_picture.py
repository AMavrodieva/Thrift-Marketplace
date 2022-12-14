# Generated by Django 4.1.4 on 2022-12-13 13:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myappuser",
            name="profile_picture",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="Profile Picture"
            ),
        ),
    ]
