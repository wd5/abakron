# -*- coding: utf-8 -*-

import datetime

from django.contrib import admin

from blogs.models import Post
from blogs.forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created = datetime.datetime.now()
        obj.save()

admin.site.register(Post, PostAdmin)