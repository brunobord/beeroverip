from django.http import Http404, HttpResponse
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list
from beers.models import Beer, NotABeer

def beer_list(request):
    return object_list(request,
        queryset=Beer.objects.order_by('name'),
    )

def beer_detail(request, slug=None):
    if not slug:
        slug = "default"
    try:
        beer = Beer.objects.get(slug=slug)
    except:
        raise Http404

    return direct_to_template(request,
        template='beers/beer_detail.html',
        extra_context={
            'beer': beer,
            'picture': beer.picture,
        },
    )

def beer_random(request):
    random_beer = Beer.objects.order_by('?')[0]
    return beer_detail(request, random_beer.slug)

def custom_404_view(request):
    response = direct_to_template(request, '404.html')
    response.status_code = 404
    return response

# drinks

def drink_detail(request, slug=None):
    if not slug:
        slug = "default"
    try:
        drink = NotABeer.objects.get(slug=slug)
    except:
        raise Http404

    return direct_to_template(request,
        template='drinks/drink_detail.html',
        extra_context={
            'drink': drink,
            'picture': drink.picture,
        },
    )

def drink_list(request):
    return object_list(request,
        queryset=NotABeer.objects.order_by('name'),
        template_name='drinks/drink_list.html',
    )

def drink_random(request):
    random_drink = NotABeer.objects.order_by('?')[0]
    return drink_detail(request, random_drink.slug)
