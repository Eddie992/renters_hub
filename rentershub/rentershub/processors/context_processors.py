from django.conf import settings


#This context processor adds the MEDIA_URL to the context.
def media(request):
    return {'media': settings.MEDIA_URL}