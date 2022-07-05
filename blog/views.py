from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
# Create your views here.

def latest(request):
    latest = Post.objects.order_by('-pub_date')
    output = []
    for p in latest:
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            'intro': p.intro,
            'body': p.body
            })
    return JsonResponse(output, safe=False)

def findOne(request, post_id):
    post = list(Post.objects.filter(id=post_id))
    output = []
    for p in post:
        output.append({
            'id': p.id,
            'published': p.published,
            'title': p.title,
            'intro': p.intro,
            'body': p.body
            })
    return JsonResponse(output, safe=False)
