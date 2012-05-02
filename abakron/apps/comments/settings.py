# -*- coding: utf-8 -*-

from django.contrib.flatpages.models import FlatPage

from comics.models import Comics
from blogs.models import Post


MODELS_MAPPINGS = {
    'blog': Post,
    'comics': Comics,
    'page': FlatPage,
}
