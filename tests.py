import os
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from models import Beer, NotABeer

class TestBeerUrls(TestCase):
    """We just have to test URLs, by the way..."""
    fixtures = ['data']

    def test_000(self):
        "not a test case, just for the user's information"
        print
        print "FYI:"
        print "num. of beers: %s" % Beer.objects.count()
        print

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
        response = self.client.get(reverse('beer_random'))
        self.assertEquals(response.status_code, 200)

    def test_rss_flow(self):
        """Testing the RSS flow"""
        response = self.client.get('/flow/beers/')
        self.assertEquals(response.status_code, 200)

    def test_url_all(self):
        """Testing '/all/' url"""
        response = self.client.get(reverse('beer_list'))
        self.assertEquals(response.status_code, 200)


class TestBeerImages(TestCase):
    """Testing image attributes"""
    fixtures = ['data']

    def test_file_existence(self):
        for beer in Beer.objects.all():
            self.assertTrue(os.path.isfile(beer.picture.file.name))

    def test_image_size(self):
        for beer in Beer.objects.all():
            self.assertTrue(max(beer.picture.height, beer.picture.width) <= 500)


class TestNotABeerUrls(TestCase):
    """We just have to test URLs, by the way..."""
    fixtures = ['notabeer']

    def test_000(self):
        "not a test case, just for the user's information"
        print
        print "FYI:"
        print "num. of drinks: %s" % NotABeer.objects.count()
        print

    def test_home(self):
        """Home page.
        Should return 'something' (this means we have a default drink)"""
        response = self.client.get('/notabeer/')
        self.assertEquals(response.status_code, 200)

    def test_404(self):
        """404 exception test."""
        response = self.client.get('/dehfzihfezihgzihgz/')
        self.assertEquals(response.status_code, 404)
        self.assertContains(response, settings.MEDIA_URL, status_code=404)

    def test_media_files(self):
        """Every drink has a picture. This picture should exist."""
        for drink in NotABeer.objects.all():
            self.assertNotEquals(drink.picture, "")
            response = self.client.get(drink.picture.url)
            self.assertEquals(response.status_code, 200)

    def test_media_file_not_found(self):
        """If any drink picture file is unknown/missing, it must be an error."""
        random_drink = NotABeer.objects.get(pk=1)
        random_drink.picture = 'unknown/file.jpg'
        random_drink.save()
        response = self.client.get(random_drink.picture.url)
        self.assertNotEquals(response.status_code, 200)

    def test_data(self):
        """Every drink has to be tested individually."""
        for drink in NotABeer.objects.all():
            response = self.client.get(drink.get_absolute_url())
            if response.status_code != 200:
                # For debug purposes.
                print drink
            self.assertEquals(response.status_code, 200)

    def test_random(self):
        """The random view should return a drink view"""
        response = self.client.get(reverse('drink_random'))
        self.assertEquals(response.status_code, 200)

##    def test_rss_flow(self):
##        """Testing the RSS flow"""
##        response = self.client.get('/flow/drinks/')
##        self.assertEquals(response.status_code, 200)

    def test_url_all(self):
        """Testing '/all/' url"""
        response = self.client.get(reverse('drink_list'))
        self.assertEquals(response.status_code, 200)

# EOF
