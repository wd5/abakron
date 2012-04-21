# -*- coding: utf-8 -*-

import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blogs.models import Post

def index(request, year=None, month=None):
    kwargs = {}
    if year:
        kwargs['created__year'] = int(year)
    if month:
        kwargs['created__month'] = int(month)

    posts = Post.objects.filter(visible=True, **kwargs).order_by('-created')

    try:
        page = int(request.GET.get('page'))
    except (TypeError, ValueError):
        page = 1

    objects = Paginator(posts, 5)

    context = {
        'posts': objects,
        'date': datetime.date(int(year), int(month), 1) if year and month else None,
        'year': year,
        'month': month,
    }

    return render(request, 'blogs/index.html', context)

def read(request, year, month, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blogs/read.html', context)
