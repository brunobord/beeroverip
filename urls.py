from django.conf.urls.defaults import *

urlpatterns = patterns('beers.views',
    (r'^(?P<slug>\w+)?/?', 'beer'),
)
