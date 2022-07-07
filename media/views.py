from django.shortcuts import render

from django.http import JsonResponse
from .models import Media
# Create your views here.

def latest(request):
    latest = Media.objects.order_by('-created_at')
    output = []
    for p in latest:
        output.append({
            'id': p.id,
            'title': p.title,
            'url': p.thumbnail.url,
            'created_at': p.created_at,
            })
    return JsonResponse(output, safe=False)

def findOne(request, media_id):
    media = list(Media.objects.filter(id=media_id))
    output = []
    for p in media:
        output.append({
            'id': p.id,
            'title': p.title,
            'url': p.thumbnail.url,
            'created_at': p.created_at,
            })
    return JsonResponse(output, safe=False)
# Create your views here.
