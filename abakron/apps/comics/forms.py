# -*- coding: utf-8 -*-

from django import forms

from comics.models import Comics


class ComicsAdminForm(forms.ModelForm):

    class Meta:
        model = Comics
        fields = ('chapter', 'title', 'image', 'alt')
