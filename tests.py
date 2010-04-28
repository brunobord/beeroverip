import os

import logging
logging.basicConfig(level=logging.CRITICAL)

from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from models import Beer, NotABeer
from models import BeerImage, NotABeerImage


class TestSettings(TestCase):
    """Testing settings"""

    def test_context_processors(self):
        """Let's make sure our context processors are okay."""
        self.assertTrue('beers.context_processors.analytics_id' in settings.TEMPLATE_CONTEXT_PROCESSORS)


class TestBeerData(TestCase):
    """Testing data / content"""
    fixtures = ['data']

    def test_max_id(self):
        """Testing if database ID are correct"""
        max_id = Beer.objects.order_by('-id')[0].id
        self.assertEquals(Beer.objects.count(), max_id)

    def test_no_duplicate_slug(self):
        """Seek for unwanted slug duplicates"""
        count = Beer.objects.count()
        slugs = set([slug[0] for slug in Beer.objects.all().values_list('slug')])
        self.assertEquals(len(slugs), count)


class TestBeerUrls(TestCase):
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
            self.assertNotEquals(beer.beerimage_set.count(), 0)

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
    
    def test_random_404(self):
        "The /random (no end slash) should not be a 404"
        response = self.client.get('/random')
        self.assertRedirects(response, reverse('beer_random'), status_code=301)

    def test_rss_flow(self):
        """Testing the RSS flow"""
        response = self.client.get('/flow/beers/')
        self.assertEquals(response.status_code, 200)

    def test_url_all(self):
        """Testing '/all/' url"""
        response = self.client.get(reverse('beer_list'))
        self.assertEquals(response.status_code, 200)


class TestMediaFiles(TestCase):
    """Testing image attributes"""
    fixtures = ['data']

    def test_media_file_url(self):
        """Every media file must exist in its filepath"""
        for image in BeerImage.objects.all():
            response = self.client.get(image.picture.url)
            self.assertEquals(response.status_code, 200)

    def test_media_file_not_found(self):
        """If any beer picture file is unknown/missing, it must be an error."""
        random_image = BeerImage.objects.get(pk=1)
        random_image.picture = 'unknown/file.jpg'
        random_image.save()
        response = self.client.get(random_image.picture.url)
        self.assertNotEquals(response.status_code, 200)

    def test_file_existence(self):
        for image in BeerImage.objects.all():
            self.assertTrue(os.path.isfile(image.picture.file.name))

    def test_image_size(self):
        for image in BeerImage.objects.all():
            self.assertTrue(max(image.picture.height, image.picture.width) <= 500)

    def test_file_is_in_images(self):
        beer_image_path = os.path.join(settings.MEDIA_ROOT, 'beers')
        for filename in os.listdir(beer_image_path):
            if filename not in ('404.jpg', ):
                logging.debug(filename)
                self.assertTrue(BeerImage.objects.get(picture='beers/%s' % filename))


class TestNotABeerUrls(TestCase):
    """We just have to test URLs, by the way..."""
    fixtures = ['notabeer']

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
        random_image = NotABeerImage.objects.get(pk=1)
        random_image.picture = 'unknown/file.jpg'
        random_image.save()
        response = self.client.get(random_image.picture.url)
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


class TestPagesUrl(TestCase):
    
    def test_about(self):
        """Testing '/about/' url"""
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        
    def test_ascii(self):
        "The magnificent ASCII beer"
        response = self.client.get(reverse('ascii'))
        self.assertEquals(response.status_code, 200)

class TestFixture(TestCase):
    
    def setUp(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        self.fixture_dir = os.path.join(self.root, 'fixtures')
    
    def test_look_for_beer_duplicate(self):
        filename = os.path.join(self.fixture_dir, 'data.json')
        data = simplejson.load(open(filename))
        raw_keys = [item['pk'] for item in data if item['model'] == 'beers.beer']
        to_check = []
        try:
            for k in raw_keys:
                if k not in to_check:
                    to_check.append(k)
                else:
                    raise Exception, k
        except:        
            assert False, "%s is a duplicate" % k
