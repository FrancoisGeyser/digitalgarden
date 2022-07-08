from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

from .models import Entry
# Create your views here.

@api_view()
def latest_entries(request):
    """
    Return a list of the latest Entries.
    """
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
    return Response(output)


@api_view()
def findOne_entry(request, entry_id):
    """
    Return a entry matching the given {id}.
    """
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
    return Response(output)


@api_view()
def search_entries(request, search_string=None):
    """
    Return a list matching the given ?search=''.
    """

    search_vector = SearchVector('title','body')

    if search_string == None:
        return Response({'message':'No search term provided'}, status=400)

    post = list(Entry.objects.annotate(search=search_vector).filter(Q(search__icontains=search_string) 
        | Q(categories__name__icontains=search_string) 
        | Q(tags__name__icontains=search_string)))

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
    return Response(output)
