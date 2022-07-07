from django.db import models
from django.utils.html import mark_safe
from filer.fields.image import FilerImageField

class Media(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = FilerImageField(null=True, blank=True,
                           related_name="media", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="auto" height="240" />'.format(self.thumbnail.url))
        return ""


