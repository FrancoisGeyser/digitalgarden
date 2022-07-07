from django.contrib import admin

# Register your models here.
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'id','title')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Media, MediaAdmin)
