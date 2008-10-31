from django.conf.urls.defaults import *

from models import Beer
from views import *
from flows import BeerFlow

flows = {
    'beers': BeerFlow,
}

urlpatterns = patterns('',
    url(r'^all/', beer_list, name="beer_list"),
    url(r'^random/', beer_random, name="beer_random"),
    url(r'^flow/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': flows}),    
    url(r'^(?P<slug>[\w-]+)?/?', beer_detail),
    url(r'^(?P<slug>[\w-]+)?/', beer_detail, name="beer_detail"),
)
