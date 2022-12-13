from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_product


UserModel = get_user_model()


class HomePageViewTest(TestCase):
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

    def test_home_page_view__when_owner__expect_to_show_page(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('home page', kwargs={'pk': user.pk}))
        self.assertEqual(200, response.status_code)

    def test_home_page_view__when_owner__expect_is_owner_true(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_home_page_view__when_no_products__expect_empty(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0, len(response.context['products']))

    def test_home_page_view__when_products__expect_show_products(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        products = [product_1, product_2]

        self.assertEqual(len(products), len(response.context['products']))

    def test_home_page_view__when_7_products_page_1__expect_show_6_products(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user)
        product_3 = create_product(user)
        product_4 = create_product(user)
        product_5 = create_product(user)
        product_6 = create_product(user)
        product_7 = create_product(user)
        products = [product_7, product_6, product_5, product_4, product_3, product_2]

        response = self.client.get(
            reverse_lazy('home page', kwargs={'pk': user.pk}),
            data={'page': 1, })

        self.assertEqual(len(products), len(response.context['page_obj']))
        self.assertListEqual(products, list(response.context['page_obj']))

    def test_home_page_view__when_7_products_page_2__expect_show_1_product(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user)
        product_3 = create_product(user)
        product_4 = create_product(user)
        product_5 = create_product(user)
        product_6 = create_product(user)
        product_7 = create_product(user)
        products = [product_1]

        response = self.client.get(
            reverse_lazy('home page', kwargs={'pk': user.pk}),
            data={'page': 2, })

        self.assertEqual(len(products), len(response.context['page_obj']))
        self.assertListEqual(products, list(response.context['page_obj']))

