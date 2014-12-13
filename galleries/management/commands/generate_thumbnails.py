from django.core.management.base import BaseCommand, CommandError
from galleries.models import Gallery

class Command(BaseCommand):
    args = '<gallery_id>'
    help = 'Creates Thumbnails for a Gallery'

    def handle(self, *args, **options):
        for gallery_id in args:
            try:
                gallery = Gallery.objects.get(pk=int(gallery_id))
                
                from django.conf import settings
                from PIL import Image as Imager
                import os

                for image in gallery.image_set.all():
                    i = Imager.open(image.image)
                    file, ext = os.path.splitext(image.image.path)
                    width, height = i.size

                    if width > height:
                       delta = width - height
                       left = int(delta/2)
                       upper = 0
                       right = height + left
                       lower = height
                    else:
                       delta = height - width
                       left = 0
                       upper = int(delta/2)
                       right = width
                       lower = width + upper

                    i = i.crop((left, upper, right, lower))
                    i.thumbnail(settings.GALLERIES_THUMBNAIL_SIZE, Imager.ANTIALIAS)
                    if ext == (".jpg" or ".JPG" or ".jpeg" or ".JPEG"):
                        i.save(file + " thumbnail.jpg") 
                    elif ext == (".png" or ".PNG"):
                        i.save(file + " thumbnail.png")
            except Gallery.DoesNotExist:
                raise CommandError('Gallery "%s" does not exist' % gallery_id)

            self.stdout.write('Successfully created images for Gallery "%s"' % gallery_id)
