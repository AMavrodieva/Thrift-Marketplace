from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_product, create_comment, create_rating, create_photo

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

    def test_details_product_view__when_some_client__expect_to_show_page(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        user_1 = self.create_user_and_login(self.SECOND_USER_DATA)
        product = create_product(user)
        photo = [create_photo(user, product)]
        comment = [create_comment(user_1, product)]
        rating = create_rating(user_1, product)

        response = self.client.get(reverse_lazy('details product', kwargs={'pk': product.pk}))

        self.assertEqual(200, response.status_code)
        self.assertEqual(product, response.context['product'])
        self.assertEqual(rating, response.context['avg_rating'])
        self.assertListEqual(comment, list(response.context['product_comments']))
        self.assertListEqual(photo, list(response.context['product_photos']))
        self.assertFalse(response.context['is_owner'])


    def test_details_product_view__when_owner__expect_to_show_page(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        user_1 = self.create_user_and_login(self.SECOND_USER_DATA)
        product = create_product(user)
        photo = [create_photo(user, product)]
        comment = [create_comment(user_1, product)]
        rating = create_rating(user_1, product)
        user = self.client.login(**self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details product', kwargs={'pk': product.pk}))

        self.assertEqual(product, response.context['product'])
        self.assertEqual(rating, response.context['avg_rating'])
        self.assertListEqual(comment, list(response.context['product_comments']))
        self.assertListEqual(photo, list(response.context['product_photos']))
        self.assertTrue(response.context['is_owner'])
