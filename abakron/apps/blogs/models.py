# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    """Blog post"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date='created')
    content = models.TextField()
    visible = models.BooleanField(default=False)
    created = models.DateTimeField()

    class Meta:
        db_table = u'blog_posts'
        ordering = ('-created',)

    def __unicode__(self):
        return self.title