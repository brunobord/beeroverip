from django.conf.urls.defaults import *
from models import Beer

info_dict = {
    'queryset': Beer.objects.order_by('slug'),
}

urlpatterns = patterns('django.views.generic',
    (r'^all/?', 'list_detail.object_list', info_dict),
)
urlpatterns += patterns('beers.views',
    (r'^random/?', 'beer_random'),
    (r'^(?P<slug>\w+)?/?', 'beer_detail'),
)
