from django import template
from galleries.models import Gallery, Image

register = template.Library()

@register.assignment_tag
def get_gallery(id):
   return Gallery.objects.get(pk=id) 
