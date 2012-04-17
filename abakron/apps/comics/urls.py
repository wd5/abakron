# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('comics.views',
    (r'^$', 'index'),
    (r'^(?P<chapter_slug>[\w-]+)/$', 'chapter'),
    (r'^(?P<chapter_slug>[\w-]+)/(?P<comics_id>\d+)/$', 'read'),
)