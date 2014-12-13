from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.management import call_command
from StringIO import StringIO
from django.contrib import messages

def generate_thumbnails(request, gallery):
    content = StringIO()
    try:
        call_command('generate_thumbnails', gallery, stdout=content)
        content = content.getvalue()
        messages.add_message(request, messages.INFO, content)
    except:
        messages.add_message(request, messages.ERROR, 'Sorry we failed to generate thumbnails')
    return redirect('/admin/galleries/gallery/')
