from django.conf.urls.defaults import patterns, url

from models import Beer
from flows import BeerFlow

# special for RSS
flows = {
    'beers': BeerFlow,
}
urlpatterns = patterns(
    '', url(
        r'^flow/(?P<url>.*)/$',
        'django.contrib.syndication.views.feed', {'feed_dict': flows}
    ),
)

# About page
about_dict = {
    'template': 'pages/about.html',
}
ascii_dict = {
    'template': 'pages/ascii.html',
}
urlpatterns += patterns(
    'django.views.generic.simple',
    url(r'^about/', 'direct_to_template', about_dict, name='about'),
    url(r'^ascii/', 'direct_to_template', ascii_dict, name='ascii'),
)

beer_dict = {
    'queryset': Beer.objects.order_by('name'),
}
urlpatterns += patterns(
    'django.views.generic.list_detail',
    url(r'^all/', 'object_list', beer_dict, name="beer_list"),
)

urlpatterns += patterns(
    'beers.views',
    # not a beer
    url(r'^notabeer/all/', 'drink_list', name='drink_list'),
    url(r'^notabeer/random/', 'drink_random', name='drink_random'),
    url(r'^notabeer/(?P<slug>[\w-]+)?/?', 'drink_detail'),
    url(r'^notabeer/(?P<slug>[\w-]+)?', 'drink_detail', name="drink_detail"),

    # beers
    url(r'^random/$', 'beer_random', name="beer_random"),
    url(r'^$', 'beer_detail'),
    url(r'^(?P<slug>[\w-]+)/', 'beer_detail', name="beer_detail"),
)
