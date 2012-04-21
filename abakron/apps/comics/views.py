# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from comics.models import Chapter, Comics
from blogs.models import Post

def index(request):
    """Latest comics"""

    try:
        post = Post.objects.latest('created')
    except Post.DoesNotExist:
        post = None

    context = {
        'obj': Comics.objects.latest('created'),
        'post': post,
    }

    return render(request, 'comics/read.html', context)

def chapter(request, chapter_slug):
    """Chapter cover"""

    try:
        post = Post.objects.latest('created')
    except Post.DoesNotExist:
        post = None

    context = {
        'obj': get_object_or_404(Chapter, slug=chapter_slug),
        'post': post,
    }

    return render(request, 'comics/chapter.html', context)

def read(request, chapter_slug, comics_position):
    """Comics view"""

    try:
        post = Post.objects.latest('created')
    except Post.DoesNotExist:
        post = None

    context = {
        'obj': get_object_or_404(Comics, chapter__slug=chapter_slug, position=comics_position),
        'post': post,
    }

    return render(request, 'comics/read.html', context)
