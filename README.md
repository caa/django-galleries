# Django Galleries (django-galleries)

A Django app which makes image galleries that may be added to any template.

You don't have to make or manage any complicated relationships with your models. Create a gallery, add your images, then display them on any page by using a template tag. 

This project is new so there'll be quite a bit of changes. I'll document these changes as well as I can.

## REQUIREMENTS
Django 1.7+, Pillow, and a database configured.

## INSTALLATION
Make sure you have specified MEDIA_ROOT and MEDIA_URL in your Django Settings File.

settings.py
```Python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galleries',
)
GALLERIES_THUMBNAIL_SIZE = (200,200)
```

urls.py
```Python
import galleries
...
    # Make sure the following line is above the "include admin.site.urls" line
    url(r'^admin/galleries/generate-thumbnails/', include('galleries.urls')),
    url(r'^admin/', include(admin.site.urls)),
```
Run the migrations
```
./manage.py migrate
```
## USAGE


### Django Template of Your Page Using get_gallery Template Tag
```HTML+Django
{% load galleries_tags %}

<style>

</style>

{% get_gallery 3 as gallery %}

{{ gallery.name }}

{% for image in gallery.image_set.all %}
<a href="{{ image.image.url }}" target="_blank"><img src="{{ image.thumbnail }}"></a>
{% endfor %}
```

The Template Tag get_gallery only retrieves the gallery specified which you can put in a variable. You can then use that data to construct the gallery.

I think I'll introduce another Template Tag display_gallery that will output all the HTML for you which you can style yourself and another one called style_gallery that will include a stylesheet and maybe one for Javascript called script_gallery.

## TASKS
-  Multiple File Upload
-  Drag & Drop Upload
-  Click & Drag Ordering
-  Image File Cleanup (Doesn't delete thumbnail files yet)
-  i18n
-  Python Packaging
-  Tests

## DESIGN DECISIONS
-  No complicated relationships with models
-  All thumbnails are squares
-  Minimal Requirements
-  Thumbnails are generated manually through a management command *generate_thumbnails* which may also be activated via a link in the galleries admin page.
