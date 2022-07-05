from django.shortcuts import render
from django.http import JsonResponse

from .models import Entry
# Create your views here.

def latest(request):
    latest = Entry.objects.order_by('-pub_date')
    output = []
    for p in latest:
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            })
    return JsonResponse(output, safe=False)

def findOne(request, entry_id):
    post = list(Entry.objects.filter(id=entry_id))
    output = []
    for p in post:
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            })
    return JsonResponse(output, safe=False)
# Create your views here.
