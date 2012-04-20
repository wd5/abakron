# -*- coding: utf-8 -*-

from django import template

from comics.models import Chapter, Comics
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('comics/tags/navigation.html')
def comics_navigation(obj, classes=None):
    """Inner navigation between comics and comics chapters

    Parameters::
        obj: instance of the model `comics.models.Chapter' or 'comics.models.Comics'
        classes: additional css classes for navigation container
    """

    left = right = last = None

    first = Chapter.objects.all().order_by('pk')[0]
    last = Comics.objects.all().select_related('chapter').order_by('-pk')[0]
    first = reverse('comics.chapters.read', args=(first.slug,))

    if isinstance(obj, Comics):
        current_comics = obj
        current_chapter = obj.chapter
        comics = list(obj.chapter.comics.all().order_by('position'))

        # Left position
        if obj.position == 1:
            left = reverse('comics.chapters.read', args=(obj.chapter.slug,))
        else:
            left_comics_id = [x for x in comics if x.pk < obj.pk][-1].position
            left = reverse('comics.read', args=(obj.chapter.slug, left_comics_id))

        # Right position
        if obj.position == len(comics):
            # Latest in chapter
            try:
                right = Chapter.objects.filter(pk__gt=obj.chapter_id).order_by('pk')[0]
                right = reverse('comics.chapters.read', args=(right.slug,))
            except IndexError:
                right = None
        else:
            try:
                right_comics_id = [x for x in comics if x.pk > obj.pk][0].position
                right = reverse('comics.read', args=(obj.chapter.slug, right_comics_id,))
            except IndexError:
                right = None

        # If we are on the latest comics
        if obj != last:
            last = reverse('comics.read', args=(last.chapter.slug, last.position))
        else:
            last = None

    else:
        current_comics = None
        current_chapter = obj
        comics = list(obj.comics.all().order_by('position'))

        try:
            left_chapter = Chapter.objects.filter(pk__lt=obj.pk).order_by('-pk')[0]
            left = reverse('comics.read', args=(left_chapter.slug, left_chapter.comics.order_by('-position').values_list('position', flat=True)[0]))
        except IndexError:
            left = None
            first = None # There is no any chapters before this

        try:
            right = reverse('comics.read', args=(obj.slug, comics[0].position))
        except IndexError:
            right = None
        last = reverse('comics.read', args=(last.chapter.slug, last.position))

    return {
        'current_comics': current_comics, # current comics if viewed
        'current_chapter': current_chapter, # current chapter cover
        'chapters': Chapter.objects.all().order_by('pk'),
        'comics': comics,
        'first': first,
        'left': left,
        'right': right,
        'last': last,
        'classes': classes,
    }