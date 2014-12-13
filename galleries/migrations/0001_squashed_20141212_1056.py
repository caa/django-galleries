# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import galleries.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'gallery',
                'verbose_name_plural': 'galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'original_height', width_field=b'original_width', max_length=255, upload_to=b'')),
                ('original_width', models.IntegerField()),
                ('original_height', models.IntegerField()),
                ('caption', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
                ('gallery', models.ForeignKey(to='galleries.Gallery')),
            ],
            options={
                'ordering': ('position',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('gallery', 'position')]),
        ),
        migrations.AlterModelTable(
            name='gallery',
            table='galleries',
        ),
        migrations.AlterModelTable(
            name='image',
            table='gallery_images',
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(height_field=b'original_height', width_field=b'original_width', max_length=255, upload_to=galleries.models.gallery_upload_path),
            preserve_default=True,
        ),
    ]
