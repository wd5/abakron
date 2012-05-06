# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from treebeard.ns_tree import NS_Node


class Comment(NS_Node):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False, db_index=True)
    created = models.DateTimeField(db_index=True)

    node_order_by = ('created',)

    class Meta:
        ordering = ('tree_id', 'lft')
