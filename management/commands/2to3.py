"""
Migrates from v2 to v3
"""
from django.core.management.base import NoArgsCommand
from django.utils import simplejson

from beers.models import Beer, BeerImage

class Command(NoArgsCommand):
    help = 'Migrates from Beeroverip v2 to v3'

    def handle_noargs(self, **options):
        # What shall I do?
        print 'Loading data file'
        data = simplejson.load(open('beers/fixtures/olddata.json'))
        for item in data:
            beer, created = Beer.objects.get_or_create(pk=item['pk'])
            fields = item['fields']
            beer.name = fields['name']
            beer.slug = fields['slug']
            beer.save()
            beerimage, created = BeerImage.objects.get_or_create(beer=beer)
            beerimage.credits = fields['credits']
            beerimage.picture = fields['picture']
            beerimage.upload_date = fields['upload_date']
            beerimage.save()
        print 'feeds data'
        print 'yay'

