from django.conf.urls.defaults import *

from models import Beer
from flows import BeerFlow

flows = {
    'beers': BeerFlow,
}

# special for RSS
urlpatterns = patterns('',
    url(r'^flow/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': flows}),
)

# About page
about_dict = {
    'template': 'pages/about.html',
}
urlpatterns += patterns('django.views.generic.simple',
    url(r'^about/', 'direct_to_template', about_dict, name='about'),
)


urlpatterns += patterns('beers.views',

    # not a beer
    url(r'^notabeer/all/', 'drink_list', name='drink_list'),
    url(r'^notabeer/random/', 'drink_random', name='drink_random'),
    url(r'^notabeer/(?P<slug>[\w-]+)?/?', 'drink_detail'),
    url(r'^notabeer/(?P<slug>[\w-]+)?', 'drink_detail', name="drink_detail"),

    # beers
    url(r'^all/', 'beer_list', name="beer_list"),
    url(r'^random/', 'beer_random', name="beer_random"),
    url(r'^(?P<slug>[\w-]+)?/?', 'beer_detail'),
    url(r'^(?P<slug>[\w-]+)?/', 'beer_detail', name="beer_detail"),
)
