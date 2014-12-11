# Django Galleries (django-galleries)

A Django app which makes image galleries that may be added to any template.

## USAGE

You don't have to make or manage any complicated relationships with your models. Create a gallery, add your images, then display them on any page by using a few template tags. 

### Django Template of Your Page
{% load galleries-tags %}

{% display_gallery 1 %}

## TASKS
-  Finish Initial Specification
-  Multiple File Upload
-  Drag & Drop Upload
-  Click & Drag Ordering
-  Image File Cleanup
-  Optional title for each gallery
-  Optional caption for each image
-  Integration into Django Admin
-  i18n
-  Python Packaging

## DESIGN DECISIONS
-  No complicated relationships with models
-  All thumbnails are squares
-  Minimal Requirements
-  Where should we specifiy thumbnail and large image dimensions? Settings file? Gallery field? display_gallery template tag? Responsive webpage makes the decision based on container size?
-  Do we ever display the original image?
-  When should the images be generated?
