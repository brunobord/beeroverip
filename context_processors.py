# context_processors
from django.conf import settings

def media_url(request):
    return {'media_url': settings.MEDIA_URL}

def analytics_id(request):
    try:
        return {'ANALYTICS_ID': settings.ANALYTICS_ID}
    except:
        return {}
