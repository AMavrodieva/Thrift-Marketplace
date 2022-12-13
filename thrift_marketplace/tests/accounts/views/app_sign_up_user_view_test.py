from django.test import TestCase
from django.urls import reverse


class AppSignUpUserViewTest(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@gmail.com',
        'password1': 'Password@12',
        'password2': 'Password@12',
    }

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )

        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'])

