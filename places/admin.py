from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ('photo', 'get_preview', 'id')
    def get_preview(self, obj):
        return format_html('<img src="{url}" max-height = 200px width = 200 />',
            url=obj.photo.url,
        )

class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
 

admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
