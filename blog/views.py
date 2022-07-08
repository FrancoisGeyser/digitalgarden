from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Post
# Create your views here.

@api_view()
def latest_posts(request):
    """
    Return a list of the most recent posts.
    """
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
    return Response(output)


@api_view()
def findOne_post(request, post_id):
    """
    Return a entry matching the given {id}.
    """
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
    return Response(output)


@api_view()
def search_posts(request,search_string=None):
    """
    Return a list matching the given ?search=''.
    """
    search_vector = SearchVector('title','intro','body')

    if search_string == None:
        return Response({'message':'No search term provided'}, status=400)

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
    return Response(output)
