"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from garden import views as garden_views
from tags import views as tags_views
from search import views as search_views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filer/', include('filer.urls')),
    path('blog/', blog_views.latest_posts, name='latestposts'),
    path('blog/<int:post_id>/', blog_views.findOne_post, name='onepost'),
    path('blog/search/<str:search_string>', blog_views.search_posts, name='postsearch'),
    path('blog/search/', blog_views.search_posts, name='postsearch'),
    path('garden/', garden_views.latest_entries, name='latestentries'),
    path('garden/<int:entry_id>/', garden_views.findOne_entry, name='oneentry'),
    path('garden/search/<str:search_string>', garden_views.search_entries, name='entrysearch'),
    path('garden/search/', garden_views.search_entries, name='entrysearch'),
    path('categories/', tags_views.list_Categories, name='listCategories'),
    path('tags/', tags_views.list_Tags, name='listTags'),
    path('search/<str:search_string>', search_views.search, name='search'),
    path('search/', search_views.search,kwargs={'search_string': None}, name='emptysearch'),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi', get_schema_view(
        title="API",
        description="Digital Code Garden",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
