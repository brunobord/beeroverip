from django.http import Http404
from django.conf import settings
from django.views.generic.simple import direct_to_template
from beers.models import Beer

def beer_detail(request, slug):
    if not slug:
        slug = "default"
    try:
        beer = Beer.objects.get(slug=slug)
    except:
        raise Http404

    return direct_to_template(request,
        template='beers/beer_detail.html',
        extra_context={'beer': beer},
    )

def beer_random(request):
    random_beer = Beer.objects.order_by('?')[0]
    return beer_detail(request, random_beer.slug)

def custom_404_view(request):
    response = direct_to_template(request, '404.html',
        extra_context={'MEDIA_URL': settings.MEDIA_URL})
    response.status_code = 404
    return response
