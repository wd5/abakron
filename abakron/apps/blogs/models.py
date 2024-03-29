# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    """Blog post"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    visible = models.BooleanField(default=False)
    created = models.DateTimeField(db_index=True)

    class Meta:
        db_table = u'blog_posts'
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blogs.read', (self.slug,), {})
