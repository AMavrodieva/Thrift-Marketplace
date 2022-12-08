from django.core import exceptions


def validator_only_letters(value):
    if not value.isalpha():
        raise exceptions.ValidationError("Ensure this value contains only letters.")


def validator_max_size_image(value):
    if value.file.size > 5 * 1024 * 1024:
        raise exceptions.ValidationError('Max file size is 5 MB')