from django.conf import settings
from django.core.urlresolvers import reverse


def analytics_id(request):
    """This context processor returns the ANALYTICS_ID extracted from the
    settings, if it does exist. If not, it returns an empty dictionary."""
    try:
        return {'ANALYTICS_ID': settings.ANALYTICS_ID}
    except:
        return {}


def drink_detail_url(request):
    """Returns the named url for 'drink_detail', since
    blocktrans doesn't allow us to use other templatetags in it."""
    return {'drink_detail_url': reverse('drink_detail')}
