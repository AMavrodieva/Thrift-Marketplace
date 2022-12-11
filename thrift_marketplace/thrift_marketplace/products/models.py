from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary import models as cloudinary_models


UserModel = get_user_model()


class Category(models.Model):
    MAX_LEN = 100
    CATEGORY = (
        ('Phones & Tablets', 'Phones & Tablets'),
        ('PCs & Laptops', 'PCs & Laptops'),
        ('TV & Audio', 'TV & Audio'),
        ('Household Appliances', 'Household Appliances'),
        ('Large Appliances', 'Large Appliances'),
        ('Health & Beauty', 'Health & Beauty'),
        ('Baby Care', 'Baby Care'),
        ('Camping & Outdoors', 'Camping & Outdoors'),
        ('Cycling', 'Cycling'),
        ('Exercise & Fitness', 'Exercise & Fitness'),
        ('Sport Apparel', 'Sport Apparel'),
        ('Sport Shoes', 'Sport Shoes'),
        ('Toys & Games', 'Toys & Games'),
        ('Baby Clothing & Shoes', 'Baby Clothing & Shoes'),
        ('Women Apparel & Shoes', ' Women Apparel & Shoes'),
        ('Men Apparel & Shoes', ' Men Apparel & Shoes'),
        ('Watches', 'Watches'),
        ('Jewellery', 'Jewellery'),
        ('All for Home', 'All for Home'),
        ('All for Garden', 'All for Garden'),
        ('All for Pets', 'All for Pets'),
        ('Other', 'Other')

    )

    name = models.CharField(
        max_length=MAX_LEN,
        choices=CATEGORY,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    PRODUCT_NAME_MIN_VALUE = 2
    PRODUCT_NAME_MAX_VALUE = 35
    DESCRIPTION_MIN_VALUE = 2
    DESCRIPTION_MAX_VALUE = 1500
    PRICE_MIN_LEN = 1.00
    LOCATION_MAX_LENGTH = 20
    IMAGE_UPLOAD_DIR = 'products/'

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT,)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,)

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_VALUE,
        validators=(
            validators.MinLengthValidator(PRODUCT_NAME_MIN_VALUE),
        ),
        null=True,
        blank=True,
        verbose_name="Product Name",
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX_VALUE,
        validators=(validators.MinLengthValidator(DESCRIPTION_MIN_VALUE),),
        null=True,
        blank=True,
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(PRICE_MIN_LEN),),
        null=False,
        blank=False,
    )

    date_of_publication = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    product_picture = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
        verbose_name="Picture"
    )

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ('-date_of_publication', )


class Photos(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    photo_picture = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
        verbose_name='Photo',
    )

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Photos"
