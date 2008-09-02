# context_processors

def analytics_id(request):
    from django.conf import settings
    try:
        return {'ANALYTICS_ID': settings.ANALYTICS_ID}
    except:
        return {}
