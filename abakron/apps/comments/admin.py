# -*- coding: utf-8 -*-

from django.contrib import admin

from treebeard.admin import TreeAdmin
from comments.models import Comment

class CommentAdmin(TreeAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
