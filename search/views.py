from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from blog.models import Post
from garden.models import Entry

def search(request):
    search_string = request.GET.get('search','')
    search_vector_blog = SearchVector('title','intro','body')
    search_vector_garden = SearchVector('title','body')

    if search_string == '':
        return JsonResponse(None, safe=False)

    post = list(Post.objects.annotate(search=search_vector_blog).filter( Q(search__icontains=search_string) 
        | Q(categories__name__icontains=search_string) 
        | Q(tags__name__icontains=search_string)))
    
    entry = list(Entry.objects.annotate(search=search_vector_garden).filter(Q(search__icontains=search_string) 
        | Q(categories__name__icontains=search_string) 
        | Q(tags__name__icontains=search_string)))

    post_output = []
    garden_output = []

    for p in post:
        tags = [tag.name for tag in p.tags.all()]
        categories = [category.name for category in p.categories.all()]
        if p.hero:
            hero = p.hero.url
        else:
            hero = None
        post_output.append({
            'id': p.id,
            'published': p.published,
            'hero': hero,
            'title': p.title,
            'intro': p.intro,
            'body': p.body,
            'tags': tags,
            'categories': categories,
            })

    for e in entry:
        tags = [tag.name for tag in e.tags.all()]
        categories = [category.name for category in e.categories.all()]
        garden_output.append({
            'id': e.id,
            'published': e.published,
            'title': e.title,
            'body': e.body,
            'tags': tags,
            'categories': categories,
            })

    output = {
            "blog": post_output,
            "garden": garden_output,
            }

    return JsonResponse(output, safe=False)
