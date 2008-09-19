from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from models import Beer

class TestUrls(TestCase):
    """We just have to test URLs, by the way..."""

    fixtures = ['data']

    def test_home(self):
        """Home page.
        Should return 'something' (this means we have a default beer)"""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_404(self):
        """404 exception test."""
        response = self.client.get('/dehfzihfezihgzihgz/')
        self.assertEquals(response.status_code, 404)
        self.assertContains(response, settings.MEDIA_URL, status_code=404)

    def test_media_files(self):
        """Every beer has a picture. This picture should exist."""
        for beer in Beer.objects.all():
            self.assertNotEquals(beer.picture, "")
            response = self.client.get(beer.picture.url)
            self.assertEquals(response.status_code, 200)

    def test_media_file_not_found(self):
        """If any beer picture file is unknown/missing, it must be an error."""
        random_beer = Beer.objects.get(pk=1)
        random_beer.picture = 'unknown/file.jpg'
        random_beer.save()
        response = self.client.get(random_beer.picture.url)
        self.assertNotEquals(response.status_code, 200)

    def test_data(self):
        """Every beer has to be tested individually."""
        for beer in Beer.objects.all():
            response = self.client.get(beer.get_absolute_url())
            if response.status_code != 200:
                # For debug purposes.
                print beer
            self.assertEquals(response.status_code, 200)

    def test_random(self):
        """The random view should return a beer view"""
        response = self.client.get("/random/")
        self.assertEquals(response.status_code, 200)
