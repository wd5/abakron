# -*- coding: utf-8 -*-

import os
from urlparse import urljoin

from django import template
from django.conf import settings

register = template.Library()


class StaticFileNode(template.Node):

    def __init__(self, filename):
        if settings.DEBUG or not settings.STATIC_DOMAINS:
            self._filename = urljoin(settings.STATIC_URL, filename)
        else:
            # select server by index based on the hash of the url
            idx = self._hash(filename) % len(settings.STATIC_DOMAINS)
            self._filename = urljoin(settings.STATIC_DOMAINS[idx], filename)
            # Appending latest modification time
            self._filename += '?v=%d' % int(os.stat(os.path.join(settings.STATIC_ROOT, filename)).st_mtime)

    @staticmethod
    def _hash(str):
        result = 0

        for idx, char in enumerate(str):
            result += ord(char)*31**(len(str)-1-idx)

        bits = 4*8

        return (result + 2**(bits-1)) % 2**bits - 2**(bits-1)

    def render(self, context):
        return self._filename

@register.tag
def static(parser, token):
    """Full URL to the file with a static-serving domain prepended"""

    _, filename = token.split_contents()

    return StaticFileNode(filename.strip('"').strip('\''))

@register.simple_tag
def static_domains_dns_prefetch():
    """HTML with a DNS prefetching instructions for all of the static domains"""

    return ''.join(['<link rel="dns-prefetch" href="%s">' % x for x in settings.STATIC_DOMAINS])
