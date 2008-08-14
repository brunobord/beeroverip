import os
from django.views.generic.simple import direct_to_template
from beers.models import Beer
from django.conf import settings

def beer(request, slug='default'):

    try:
        beer = Beer.objects.get(slug=slug)
        picture = beer.picture
    except:
        picture = 'beers/default.jpg'

    picture = os.path.join(settings.MEDIA_URL, picture)

    return direct_to_template(request, 'default.html', extra_context={'picture': picture})
