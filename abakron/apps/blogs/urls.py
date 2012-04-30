# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('blogs.views',
    url(r'^$', 'index', name='blogs.index'),
    url(r'^(?P<slug>[\w-]+)/$', 'read', name='blogs.read'),
)