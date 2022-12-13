from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_product, create_request


UserModel = get_user_model()


class AppDetailsUserViewTest(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@gmail.com',
        'password': 'Password@12',
    }

    SECOND_USER_DATA = {
        'username': 'test_user_1',
        'email': 'test_user_1@gmail.com',
        'password': 'Password@12',
    }

    def create_user_and_login(self, user_date):
        user = UserModel.objects.create_user(**user_date)
        self.client.login(**user_date)
        return user

    def test_details_user_view__when_owner__expect_is_owner_true(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_details_user_view__when_no_request__expect_empty(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0, len(response.context['send_queries']))

    def test_details_user_view__when_request__expect_show_request(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        user_1 = UserModel.objects.create_user(**self.SECOND_USER_DATA)
        product = create_product(user_1)
        product_request = [create_request(user, product)]
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(len(product_request), len(response.context['send_queries']))
        self.assertListEqual(product_request, list(response.context['send_queries']))

