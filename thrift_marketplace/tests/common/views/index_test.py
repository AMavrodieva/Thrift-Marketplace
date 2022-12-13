import requests
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_product
from thrift_marketplace.common.forms import SearchProductsForm, SearchCategoryForm

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

    def test_index_view__when_no_products__expect_empty(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('index'))

        self.assertEqual(0, len(response.context['products']))
        self.assertEqual(0, len(response.context['page_obj']))

    def test_index_view__when_products__expect_show_products(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        user_1 = UserModel.objects.create_user(**self.SECOND_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user_1)
        response = self.client.get(reverse_lazy('index'))
        products = [product_2, product_1]

        self.assertEqual(len(products), len(response.context['products']))
        self.assertListEqual(products, list(response.context['products']))
        self.assertEqual(len(products), len(response.context['page_obj']))
        self.assertListEqual(products, list(response.context['page_obj']))

    def test_index_view__when_7_products_page_1__expect_show_6_products(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        user_1 = UserModel.objects.create_user(**self.SECOND_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user_1)
        product_3 = create_product(user)
        product_4 = create_product(user_1)
        product_5 = create_product(user_1)
        product_6 = create_product(user)
        product_7 = create_product(user_1)
        products = [product_7, product_6, product_5, product_4, product_3, product_2]

        response = self.client.get(
            reverse_lazy('index'),
            data={'page': 1, })

        self.assertEqual(len(products), len(response.context['page_obj']))
        self.assertListEqual(products, list(response.context['page_obj']))

    def test_home_page_view__when_7_products_page_2__expect_show_1_product(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        user_1 = UserModel.objects.create_user(**self.SECOND_USER_DATA)
        product_1 = create_product(user)
        product_2 = create_product(user_1)
        product_3 = create_product(user)
        product_4 = create_product(user_1)
        product_5 = create_product(user_1)
        product_6 = create_product(user)
        product_7 = create_product(user_1)
        products = [product_1]
        response = self.client.get(
            reverse_lazy('index'),
            data={'page': 2, })

        self.assertEqual(len(products), len(response.context['page_obj']))
        self.assertListEqual(products, list(response.context['page_obj']))

