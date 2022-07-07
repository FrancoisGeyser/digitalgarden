from django.db import models
from ckeditor.fields import RichTextField
from tags.models import Category, Tag

# Create your models here.
class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField()
    title = models.CharField(max_length=200)
    intro = RichTextField()
    body = RichTextField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
