from django.db import models
from django.utils.safestring import mark_safe
import os

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'galleries'
        verbose_name_plural = 'galleries'

    def generate_thumbnails(self):
        return mark_safe("<a href='/admin/galleries/generate-thumbnails/%s/'>Generate Thumbnails for %s</a>") % (self.id, self.name,)
    generate_thumbnails.allow_tags = True
    generate_thumbnails.short_description = ("Execute")

def gallery_upload_path(self, filename):
    return "galleries/%s/%s" % (self.gallery_id, filename)

class Image(models.Model):
    image = models.ImageField(max_length=255, width_field='original_width', height_field='original_height',
                              upload_to=gallery_upload_path)
    original_width = models.IntegerField()
    original_height = models.IntegerField()
    caption = models.CharField(max_length=100, blank=True)
    gallery = models.ForeignKey(Gallery)
    position = models.IntegerField()

    class Meta:
        db_table = 'gallery_images'
        ordering = ("position",)
        unique_together = ("gallery", "position")

    def thumbnail(self):
        file, ext = os.path.splitext(self.image.url)
        if ext in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            return mark_safe(file + " thumbnail.jpg")
        elif ext in (".png", ".PNG"):
            return mark_safe(file + " thumbnail.png")

from django.db.models.signals import post_delete 
from django.dispatch.dispatcher import receiver

@receiver(post_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(save=False) # TASK add exception handling here

# TASK delete Gallery media folder signal
