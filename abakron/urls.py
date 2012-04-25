# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from comics.feeds import AggregatedFeed

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^blog/', include('blogs.urls')),
    (r'^faq/', include('faq.urls')),
    (r'^auth/', include('social_auth.urls')),

    url(r'^feed/$', AggregatedFeed(), name='feed'),
    (r'^api/urls/', include('jsroutes.urls')),
    (r'^api/comics/', include('comics.api')),

    (r'^', include('comics.urls')),
)
