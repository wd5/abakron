# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('comics.views',
    url(r'^$', 'index', name='comics.index'),
    url(r'^(?P<chapter_slug>[\w-]+)/$', 'chapter', name='comics.chapters.read'),
    url(r'^(?P<chapter_slug>[\w-]+)/(?P<comics_position>\d+)/$', 'read', name='comics.read'),
)