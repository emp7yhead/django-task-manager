from django.test import TestCase


class IndexPageViewTest(TestCase):
    def test_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task Manager")