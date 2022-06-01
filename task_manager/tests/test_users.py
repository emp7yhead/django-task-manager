"""Tests for users app."""
from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from faker import Faker


class LoginUserTest(TestCase):
    """Test user login."""

    def setUp(self):
        """Create test user."""
        self.faker = Faker()
        self.username = self.faker.user_name()
        self.password = self.faker.password(length=10)
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
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
                'username': self.username,
                'password': self.password,
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def _test_wrong_username(self):
        response = self.client.post(
            '/login/',
            {
                'username': 'wrong',
                'password': self.password,
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)

    def _test_wrong_password(self):
        response = self.client.post(
            '/login/',
            {
                'username': self.username,
                'password': 'wrong',
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)
