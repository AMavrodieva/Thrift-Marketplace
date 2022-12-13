from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from cloudinary import models as cloudinary_models

from thrift_marketplace.accounts.validators import validator_only_letters


class MyAppUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_VALUE = 2
    FIRST_NAME_MAX_VALUE = 20
    LAST_NAME_MIN_VALUE = 2
    LAST_NAME_MAX_VALUE = 30
    FIRST_NAME_ERROR_MESSAGE = "First name must be a minimum of 2 chars"
    LAST_NAME_ERROR_MESSAGE = "Last name must be a minimum of 2 chars"
    IMAGE_UPLOAD_DIR = 'profiles/'
    PHONE_NUMBER_MAX_VALUE = 20

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        error_messages={'unique': "A user with that email already exists.", },
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_VALUE,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_VALUE, FIRST_NAME_ERROR_MESSAGE),
            validator_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_VALUE,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_VALUE, LAST_NAME_ERROR_MESSAGE),
            validator_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name="Last Name",
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_VALUE,
        null=True,
        blank=True,
        verbose_name="Phone Number"
    )

    profile_picture = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    def __str__(self):
        return self.username
