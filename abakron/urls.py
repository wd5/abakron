# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^blog/', include('blogs.urls')),

    (r'^api/urls/', include('jsroutes.urls')),
    (r'^api/comics/', include('comics.api')),

    (r'^', include('comics.urls')),
)
