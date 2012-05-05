# -*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from comments.forms import CommentForm
from comments.models import Comment
from comments.settings import MODELS_MAPPINGS

register = template.Library()


class CommentsNode(template.Node):

    reverse_models_mappings = dict((v, k) for k, v in MODELS_MAPPINGS.iteritems())

    def __init__(self, obj):
        self._obj = template.Variable(obj)

    def render(self, context):
        obj = self._obj.resolve(context)

        content_type = ContentType.objects.get_for_model(obj)
        form = CommentForm()

        template_context = {
            'request': context['request'],
            'comments': Comment.objects.filter(content_type=content_type, object_id=obj.pk).order_by('tree_id', 'created'),
            'form': form,
            'action_url': reverse('api.comments', args=(self.reverse_models_mappings[content_type.model_class()], obj.pk)),
        }

        return render_to_string('comments/tags/comments.html', template_context)

@register.tag
def comments(parser, token):
    """{% comments obj %}"""

    bits = token.split_contents()

    return CommentsNode(bits[1])


@register.inclusion_tag('comments/tags/comments_count.html')
def comments_count(obj):
    ct = ContentType.objects.get_for_model(obj)

    return {
        'obj': obj,
        'count': Comment.objects.filter(content_type=ct, object_id=obj.pk, is_deleted=False).count(),
    }