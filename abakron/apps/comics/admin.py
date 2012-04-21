# -*- coding: utf-8 -*-

import datetime

from django.contrib import admin
from pytils.translit import slugify

from comics.models import Chapter, Comics
from comics.forms import ComicsAdminForm

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', lambda x: x.comics.all().count())

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created = datetime.datetime.now()

        obj.save()

admin.site.register(Chapter, ChapterAdmin)


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter')
    list_filter = ('chapter',)
    list_select_related = True
    form = ComicsAdminForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created = datetime.datetime.now()

        obj.position = Comics.objects.filter(chapter=obj.chapter, created__lt=obj.created).count()+1
        obj.save()

admin.site.register(Comics, ComicsAdmin)
