# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from djangorestframework.resources import ModelResource
from djangorestframework.views import ListModelView
from utils.api import ReadModelView

from comics.models import Chapter, Comics


class ChapterResource(ModelResource):

    model = Chapter
    fields = ('id', 'title', 'slug', 'cover_url')

    def cover_url(self, instance):
        return instance.cover.url


class ComicsResource(ModelResource):

    model = Comics
    fields = ('id', 'chapter', 'title', 'image_url', 'alt', 'position')

    def image_url(self, instance):
        return instance.image.url


urlpatterns = patterns('',
    url(r'^chapter/$', ListModelView.as_view(resource=ChapterResource), name='api.comics.chapters'),
    (r'^chapter/(?P<pk>\d+)/$', ReadModelView.as_view(resource=ChapterResource)),

    url(r'^comics/$', ListModelView.as_view(resource=ComicsResource), name='api.comics'),
    (r'^comics/(?P<pk>\d+)/$', ReadModelView.as_view(resource=ComicsResource)),
)