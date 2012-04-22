# -*- coding: utf-8 -*-

from django.contrib import admin
import markdown

from faq.models import Entry
from faq.forms import EntryAdminForm


class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'have_answer', 'created')
    list_select_related = True
    fields = ('question_markdown', 'answer')
    readonly_fields = ('question_markdown',)
    form = EntryAdminForm

    def have_answer(self, obj):
        return len(obj.answer) > 0
    have_answer.boolean = True

    def question_markdown(self, obj):
        return markdown.markdown(obj.question)
    question_markdown.short_description = u'Question'
    question_markdown.allow_tags = True

admin.site.register(Entry, EntryAdmin)