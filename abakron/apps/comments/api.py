# -*- coding: utf-8 -*-
import datetime

from django.conf.urls import patterns, url
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from djangorestframework import status
from djangorestframework.resources import ModelResource
from djangorestframework.response import ErrorResponse, Response
from djangorestframework.views import View

from comments.models import Comment
from comments.forms import CommentForm
from comments.settings import MODELS_MAPPINGS


class ListView(View):
    fields = ('id',)

    def get(self, request, *args, **kwargs):
        ct = ContentType.objects.get_for_model(MODELS_MAPPINGS[kwargs['model']])

        try:
            ct.get_object_for_this_type(pk=kwargs['object_id'])
        except ObjectDoesNotExist:
            raise ErrorResponse(status.HTTP_404_NOT_FOUND)

        queryset = Comment.objects.filter(content_type=ct, object_id=kwargs['object_id']).select_related('user') \
            .order_by('created')

        return [{
            'id': x.id,
            'created': x.created,
            'content': x.content,
            'depth': x.depth,
            'user': {
                'id': x.user.id,
                'username': x.user.username,
            }
        } for x in queryset]

    def post(self, request, *args, **kwargs):
        ct = ContentType.objects.get_for_model(MODELS_MAPPINGS[kwargs['model']])

        try:
            obj = ct.get_object_for_this_type(pk=kwargs['object_id'])
        except ObjectDoesNotExist:
            raise ErrorResponse(status.HTTP_404_NOT_FOUND)

        form = CommentForm(request.POST)
        if not form.is_valid():
            raise ErrorResponse(status.HTTP_400_BAD_REQUEST)

        data = {
            'content_type': ct,
            'object_id': kwargs['object_id'],
            'user': request.user,
            'created': datetime.datetime.now(),
            'content': form.cleaned_data['content'],
        }

        parent = form.cleaned_data['parent']
        if parent:
            instance = parent.add_child(**data)
        else:
            instance = Comment.add_root(**data)

        response = {
            'id': instance.pk,
            'content': instance.content,
            'created': instance.created,
            'depth': instance.depth,
        }

        if request.is_ajax():
            return Response(status.HTTP_201_CREATED)
        return HttpResponseRedirect(obj.get_absolute_url())

class CommentResource(ModelResource):

    model = Comment
    form = CommentForm
    fields = ('id', 'user__username', 'depth', 'content', 'created')

urlpatterns = patterns('',
    url(r'(?P<model>%s)/(?P<object_id>\d+)/' % '|'.join(MODELS_MAPPINGS.keys()),
        ListView.as_view(), name='api.comments'),
)