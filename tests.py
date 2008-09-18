from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from models import Beer

class TestUrls(TestCase):
    fixtures = ['data']
    def setUp(self):
        pass

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_404(self):
        response = self.client.get('/dehfzihfezihgzihgz/')
        self.assertEquals(response.status_code, 404)
        self.assertContains(response, settings.MEDIA_URL, status_code=404)

    def test_media_files(self):
        for beer in Beer.objects.all():
            self.assertNotEquals(beer.picture, "")
            response = self.client.get(beer.picture.url)
            self.assertEquals(response.status_code, 200)

    def test_data(self):
        for beer in Beer.objects.all():
            response = self.client.get(beer.get_absolute_url())
            if response.status_code != 200:
                print beer
            self.assertEquals(response.status_code, 200)

    def test_random(self):
        response = self.client.get("/random/")
        self.assertEquals(response.status_code, 200)
