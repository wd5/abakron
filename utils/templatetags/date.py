# -*- coding: utf-8 -*-

from django import template

from pytils.dt import ru_strftime

register = template.Library()

@register.filter
def ru_strftime_plain(date, format='%d.%m.%Y'):
    print date
    return ru_strftime(format, date)