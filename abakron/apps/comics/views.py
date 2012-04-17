# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from comics.models import Chapter, Comics

def index(request):
    """Latest comics"""

    raise NotImplementedError()

def chapter(request, chapter_slug):
    """Chapter cover"""

    raise NotImplementedError()

def read(request, chapter_slug, comics_id):
    """Comics view"""

    raise NotImplementedError()