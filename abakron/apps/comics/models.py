# -*- coding: utf-8 -*-

import os

from django.db import models
from pytils.translit import slugify
from utils.files.storage.overwrite import OverwriteStorage

def chapter_cover_upload(instance, filename):
    return 'comics/%(slug)s/cover%(ext)s' % {
        'slug': instance.slug,
        'ext': os.path.splitext(filename)[1],
    }


class Chapter(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    cover = models.ImageField(upload_to=chapter_cover_upload, storage=OverwriteStorage())

    class Meta:
        db_table = 'comics_chapters'
        verbose_name = u'chapter'
        verbose_name_plural = u'chapters'

    def __unicode__(self):
        return self.title


def comics_upload(instance, filename):
    return 'comics/%(slug)s/%(position)03d%(ext)s' % {
        'slug': instance.chapter.slug,
        'position': Comics.objects.filter(chapter=instance.chapter_id, created__lt=instance.created).count()+1,
        'ext': os.path.splitext(filename)[1],
    }


class Comics(models.Model):

    chapter = models.ForeignKey(Chapter, related_name='comics')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=comics_upload, storage=OverwriteStorage())
    alt = models.CharField(max_length=255)
    created = models.DateTimeField()
    position = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        db_table = 'comics_comics'
        unique_together = (('chapter', 'position'),)
        verbose_name = u'comics'
        verbose_name_plural = u'comics'

    def __unicode__(self):
        return self.title
