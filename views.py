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
