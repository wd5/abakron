# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render, redirect

from faq.models import Entry
from faq.forms import EntryForm

def index(request):

    if request.user.is_authenticated() and request.POST:
        form = EntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.created = datetime.datetime.now()
            instance.save()

            return redirect('.')

    else:
        form = EntryForm()

    # TODO: pagination
    entries = Entry.objects.filter(visible=True).order_by('-created')

    context = {
        'entries': entries,
        'form': form,
    }

    return render(request, 'faq/index.html', context)