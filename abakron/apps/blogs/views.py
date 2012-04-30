# -*- coding: utf-8 -*-

import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blogs.models import Post

def index(request):
    posts = Post.objects.filter(visible=True).order_by('-created')

    try:
        page = int(request.GET.get('page'))
    except (TypeError, ValueError):
        page = 1

    objects = Paginator(posts, 5)

    context = {
        'posts': objects,
    }

    return render(request, 'blogs/index.html', context)

def read(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blogs/read.html', context)
