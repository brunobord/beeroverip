# context_processors
from django.conf import settings

def analytics_id(request):
    try:
        return {'ANALYTICS_ID': settings.ANALYTICS_ID}
    except:
        return {}
