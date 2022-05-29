"""Test for index page view."""
from http import HTTPStatus

from django.test import TestCase


class IndexPageViewTest(TestCase):
    """Test for index page."""

    def test_page(self):
        """Tests page that the response to GET is valid."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Task Manager")
