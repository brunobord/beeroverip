from django.test import TestCase
from django.test.client import Client

class TestUrls(TestCase):
    fixtures = ['data']
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
