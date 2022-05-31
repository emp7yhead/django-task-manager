"""Test for index page view."""
from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class IndexPageViewTest(TestCase):
    """Test for index page."""

    def test_page(self):
        """Tests page that the response to GET is valid."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class LoginPageViewTest(TestCase):
    """Test user signin."""

    fake_user = {
        'username': 'test',
        'password': 'random_password1',
    }

    def setUp(self):
        """Create test user."""
        self.user = User.objects.create_user(
            username=self.fake_user['username'],
            password=self.fake_user['password'],
        )
        self.user.save()

    def tearDown(self):
        """Delete test user."""
        self.user.delete()

    def test(self):
        """Send registration request."""
        response = self.client.get(
            reverse_lazy('login'),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self._test_correct()
        self._test_wrong_password()
        self._test_wrong_username()

    def _test_correct(self):
        response = self.client.post(
            '/login/',
            {
                'username': self.fake_user['username'],
                'password': self.fake_user['password'],
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def _test_wrong_username(self):
        response = self.client.post(
            '/login/',
            {
                'username': 'wrong',
                'password': self.fake_user['password'],
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)

    def _test_wrong_password(self):
        response = self.client.post(
            '/login/',
            {
                'username': self.fake_user['username'],
                'password': 'wrong',
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)
