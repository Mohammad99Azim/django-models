from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SnacksTest(TestCase):
    def test_list_view_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_list_view_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'snack_list.html')