from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Tag,Category

def list_Categories(request):
    all_categories = list(Category.objects.all())
    output = [category.name for category in all_categories]

    return JsonResponse(output, safe=False)

def list_Tags(request):
    all_tags = list(Tag.objects.all())
    output = [tag.name for tag in all_tags]

    return JsonResponse(output, safe=False)
