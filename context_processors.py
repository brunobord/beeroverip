from django.conf import settings
from django.core.urlresolvers import reverse


def analytics_id(request):
    """This context processor returns the ANALYTICS_ID extracted from the
    settings, if it does exist. If not, it returns an empty dictionary."""
    try:
        return {'ANALYTICS_ID': settings.ANALYTICS_ID}
    except:
        return {}

