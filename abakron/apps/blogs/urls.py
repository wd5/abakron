# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('blogs.views',
    url(r'^$', 'index', name='blogs.index'),
    url(r'^(?P<year>\d{4})/$', 'index', name='blogs.year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'index', name='blogs.month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[\w-]+)/$', 'read', name='blogs.read'),
)