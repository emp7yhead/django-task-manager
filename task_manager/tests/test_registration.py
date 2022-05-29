"""Test for user registration."""
from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.forms import RegisterAndUpdateUserForm


class RegistrationPageViewTest(TestCase):
    """Test common registration page view."""

    def setUp(self):
        """Create a test database."""
        self.client: Client = Client()

    def test(self):
        """Send get request, and check data page assertions."""
        response = self.client.get(
            reverse_lazy('registration'),
        )
        form_fields = RegisterAndUpdateUserForm.base_fields
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self._assert_username(form_fields, response)
        self._assert_first_name(form_fields, response)
        self._assert_last_name(form_fields, response)
        self._assert_password(form_fields, response)
        self._assert_password_confiramtion(form_fields, response)

    def _assert_first_name(self, form_fields, response):
        self.assertIn(
            str(form_fields['first_name'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['first_name'].help_text),
            response.rendered_content,
        )

    def _assert_last_name(self, form_fields, response):
        self.assertIn(
            str(form_fields['last_name'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['last_name'].help_text),
            response.rendered_content,
        )

    def _assert_username(self, form_fields, response):
        self.assertIn(
            str(form_fields['username'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['username'].help_text),
            response.rendered_content,
        )

    def _assert_password(self, form_fields, response):
        self.assertIn(
            str(form_fields['password1'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['password1'].help_text),
            response.rendered_content,
        )

    def _assert_password_confiramtion(self, form_fields, response):
        self.assertIn(
            str(form_fields['password2'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['password2'].help_text),
            response.rendered_content,
        )


class SuccessRegistrationTest(TestCase):
    """Test user registration."""

    fake_user = {
        'first_name': 'name',
        'last_name': 'surname',
        'username': 'test',
        'password': 'random_password1',
    }

    def setUp(self):
        """Create a test database."""
        self.client: Client = Client()

    def test(self):
        """Send valid registration request."""
        first_name = self.fake_user['first_name']
        last_name = self.fake_user['last_name']
        username = self.fake_user['username']
        password = self.fake_user['password']
        response = self.client.post(
            reverse_lazy('registration'),
            data={
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'password1': password,
                'password2': password,
            },
        )
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(
            User.objects.filter(first_name=first_name, username=username),
        )
