from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Post
# Create your views here.

def latest(request):
    latest = Post.objects.order_by('-pub_date')
    output = []
    for p in latest:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        if p.hero:
            hero = p.hero.url
        else:
            hero = None

        output.append({
            'id': p.id,
            'published': p.published,
            'hero': hero,
            'title': p.title,
            'intro': p.intro,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)

def findOne(request, post_id):
    post = list(Post.objects.filter(id=post_id))
    output = []
    for p in post:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        if p.hero:
            hero = p.hero.url
        else:
            hero = None
        output.append({
            'id': p.id,
            'published': p.published,
            'hero': hero,
            'title': p.title,
            'intro': p.intro,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)


def search(request):
    search_string = request.GET.get('search','')
    search_vector = SearchVector('title','intro','body')

    post = list(Post.objects.annotate(search=search_vector).filter( Q(search__icontains=search_string) 
        | Q(categories__name__icontains=search_string) 
        | Q(tags__name__icontains=search_string)))
    output = []
    for p in post:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        if p.hero:
            hero = p.hero.url
        else:
            hero = None
        output.append({
            'id': p.id,
            'published': p.published,
            'hero': hero,
            'title': p.title,
            'intro': p.intro,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })
    return JsonResponse(output, safe=False)
