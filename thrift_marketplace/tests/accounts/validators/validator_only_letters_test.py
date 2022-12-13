from unittest import TestCase

from django.core.exceptions import ValidationError

from thrift_marketplace.accounts.validators import validator_only_letters


class OnlyLettersValidatorTests(TestCase):
    def test_only_letter_validator__when_valid__expect_ok(self):
        validator_only_letters('Aneliya')

    def test_only_letter_validator__when_name_has_digits__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validator_only_letters('Aneliya9')

        self.assertIsNotNone(context.exception)

    def test_only_letter_validator__when_name_has_only_digits__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validator_only_letters('12345678910')

        self.assertIsNotNone(context.exception)

    def test_only_letter_validator__when_name_has_symbols__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validator_only_letters('Ani@_')

        self.assertIsNotNone(context.exception)

    def test_only_letter_validator__when_None__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validator_only_letters('')

        self.assertIsNotNone(context.exception)

