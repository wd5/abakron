# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from comics.models import Chapter, Comics
from blogs.models import Post

def index(request):
    """Latest comics"""

    context = {
        'obj': Comics.objects.latest('created'),
        'post': Post.objects.latest('created'),
    }

    return render(request, 'comics/read.html', context)

def chapter(request, chapter_slug):
    """Chapter cover"""

    context = {
        'obj': get_object_or_404(Chapter, slug=chapter_slug),
        'post': Post.objects.latest('created'),
    }

    return render(request, 'comics/chapter.html', context)

def read(request, chapter_slug, comics_position):
    """Comics view"""

    context = {
        'obj': get_object_or_404(Comics, chapter__slug=chapter_slug, position=comics_position),
        'post': Post.objects.latest('created'),
    }

    return render(request, 'comics/read.html', context)
