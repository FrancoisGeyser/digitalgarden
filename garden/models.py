from django.db import models

# Create your models here.
class Entry(models.Model):
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField()
    title = models.CharField(max_length=200)


