# -*- coding: utf-8 -*-

import itertools

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
import markdown

from comics.models import Chapter, Comics
from blogs.models import Post

class AggregatedFeed(Feed):
    title = u'Абакрон'
    description = u''

    def __init__(self):
        self._site = Site.objects.get_current()
        super(AggregatedFeed, self).__init__()

    @property
    def link(self):
        return 'http://%s' % self._site.domain

    def items(self):
        chapters = list(Chapter.objects.all().order_by('-created')[:10])
        comics = list(Comics.objects.all().order_by('-created')[:10])
        posts = list(Post.objects.filter(visible=True).order_by('-created')[:10])

        return sorted(chapters+comics+posts, key=lambda x: x.created, reverse=True)[:20]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        if isinstance(item, Chapter):
            return u'<a href="%(url)s"><img src="%(src)s" alt="%(title)s" title="%(title)s"></a>' % {
                'src': item.cover.url,
                'title': item.title,
                'url': 'http://%s%s' % (self._site.domain, item.get_absolute_url()),
            }
        elif isinstance(item, Comics):
            return u'<a href="%(url)s"><img src="%(src)s" alt="%(alt)s" title="%(title)s"></a>' % {
                'src': item.image.url,
                'alt': item.alt,
                'title': item.title,
                'url': 'http://%s%s' % (self._site.domain, item.get_absolute_url()),
            }
        else:
            return markdown.markdown(item.content)