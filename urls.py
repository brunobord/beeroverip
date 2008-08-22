from django.conf.urls.defaults import *
from models import Beer

info_dict = {
    'queryset': Beer.objects.order_by('slug'),
}
info_dict_detail = info_dict.update({
    'slug_field': 'slug',
    'template_object_name': 'beer',
    'slug': 'default',
})

urlpatterns = patterns('django.views.generic',
    (r'^all/?', 'list_detail.object_list', info_dict),
    (r'^(?P<slug>\w+)?/?', 'list_detail.object_detail', info_dict),
)
