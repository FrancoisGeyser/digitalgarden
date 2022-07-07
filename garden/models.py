from django.db import models
from tags.models import Category, Tag
from ckeditor.fields import RichTextField

# Create your models here.
class Entry(models.Model):
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField()
    title = models.CharField(max_length=200)
    body = RichTextField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


