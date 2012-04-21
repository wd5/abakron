# -*_ coding: utf-8 -*-

from django import forms

from blogs.models import Post


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'visible')
