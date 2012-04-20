# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from comics.models import Chapter, Comics

def index(request):
    """Latest comics"""

    obj = Comics.objects.latest('created')

    context = {
        'obj': obj,
    }

    return render(request, 'comics/read.html', context)

def chapter(request, chapter_slug):
    """Chapter cover"""

    obj = get_object_or_404(Chapter, slug=chapter_slug)

    context = {
        'obj': obj,
    }

    return render(request, 'comics/chapter.html', context)

def read(request, chapter_slug, comics_position):
    """Comics view"""

    obj = get_object_or_404(Comics, chapter__slug=chapter_slug, position=comics_position)

    context = {
        'obj': obj,
    }

    return render(request, 'comics/read.html', context)
