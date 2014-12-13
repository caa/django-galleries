from django.contrib import admin
from models import Gallery, Image

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'caption', 'position',)
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'generate_thumbnails',)
    list_display_links = ('name', 'description',)
    inlines = [ImageInline]
    search_fields = ('name', 'description',)

admin.site.register(Gallery, GalleryAdmin)

