from beers.models import Beer
from django.views.generic.list_detail import object_detail

def beer_detail(request, slug):
    if not slug:
        slug = "default"
    queryset = Beer.objects.order_by('slug')
    return object_detail(request,
        queryset = queryset,
        slug = slug,
        slug_field = 'slug',
        template_object_name = 'beer',
    )

def beer_random(request):
    random_beer = Beer.objects.order_by('?')[0]
    return beer_detail(request, random_beer.slug)
