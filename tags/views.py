from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Tag,Category

@api_view()
def list_Categories(request):
    """
    Return a list of all the existing categories.
    """
    all_categories = list(Category.objects.all())
    output = [category.name for category in all_categories]

    return Response(output)

@api_view()
def list_Tags(request):
    """
    Return a list of all the existing tags.
    """
    all_tags = list(Tag.objects.all())
    output = [tag.name for tag in all_tags]

    return Response(output)
