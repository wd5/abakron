# -*- coding: utf-8 -*-

from django import forms

from faq.models import Entry


class EntryForm(forms.ModelForm):
    """FAQ entry form for user"""

    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': u'Спросите нас что-нибудь!'}))

    class Meta:
        model = Entry
        fields = ('question',)


class EntryAdminForm(forms.ModelForm):
    """FAQ entry form for admin"""

    class Meta:
        model = Entry
        fields = ('answer', 'visible')
