# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment


class CommentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ('content',)
