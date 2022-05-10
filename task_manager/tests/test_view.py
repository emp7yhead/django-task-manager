from django.test import TestCase


class IndexPageViewTest(TestCase):
    """Test for index page."""

    status_code = 200

    def test_page(self):
        """Tests page that the response to GET is valid."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code)
        self.assertContains(response, "Task Manager")
