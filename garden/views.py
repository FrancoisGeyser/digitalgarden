from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse

from .models import Entry
# Create your views here.

def latest(request):
    latest = Entry.objects.order_by('-pub_date')
    output = []
    for p in latest:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)

def findOne(request, entry_id):
    post = list(Entry.objects.filter(id=entry_id))
    output = []
    for p in post:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)

def searchOne(request):
    search_string = request.GET.get('search','')
    search_vector = SearchVector('title','body')

    post = list(Entry.objects.annotate(search=search_vector).filter(search__icontains=search_string))
    output = []
    for p in post:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)
