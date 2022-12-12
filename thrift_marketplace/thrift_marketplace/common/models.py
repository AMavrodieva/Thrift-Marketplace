from django.contrib.auth import get_user_model
from django.db import models

from thrift_marketplace.products.models import Product

UserModel = get_user_model()


class ProductComment(models.Model):

    TEXT_MAX_LEN = 300

    text = models.CharField(
        max_length=TEXT_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Comments"
    )

    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text


class ProductRequest(models.Model):
    QUERY_MAX_LEN = 300

    text = models.TextField(
        null=False,
        blank=False,
        verbose_name="Request"
    )

    request_email = models.EmailField(
        null=False,
        blank=False,
        verbose_name="Your Email"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    request_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('pk',)


class ProductRating(models.Model):
    RATING_MAX_LEN = 1
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
    )

    review_rating = models.CharField(
        max_length=RATING_MAX_LEN,
        choices=RATING,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.review_rating
