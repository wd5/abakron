# -*- coding: utf-8 -*-

from django.contrib import admin

from faq.models import Entry
from faq.forms import EntryAdminForm


class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'have_answer', 'created')
    list_select_related = True
    fields = ('question', 'answer')
    readonly_fields = ('question',)
    form = EntryAdminForm

    def have_answer(self, obj):
        return len(obj.answer) > 0
    have_answer.boolean = True

admin.site.register(Entry, EntryAdmin)