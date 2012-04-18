# -*- coding: utf-8 -*-

from django import template

from comics.models import Chapter, Comics

register = template.Library()

@register.inclusion_tag('comics/tags/navigation.html')
def comics_navigation(obj, classes=None):
    """Inner navigation between comics and comics chapters

    Parameters::
        obj: instance of the model `comics.models.Chapter' or 'comics.models.Comics'
        classes: additional css classes for navigation container
    """

    if isinstance(obj, Comics):
        current_comics = obj
        current_chapter = obj.chapter
        comics = list(obj.chapter.comics.all().order_by('position'))
    else:
        current_comics = None
        current_chapter = obj
        comics = obj.comics.all().order_by('position')

    return {
        'current_comics': current_comics, # current comics if viewed
        'current_chapter': current_chapter, # current chapter cover
        'chapters': Chapter.objects.all().order_by('pk'),
        'comics': comics,
        'first': None,
        'left': None,
        'right': None,
        'last': None,
        'classes': classes,
    }