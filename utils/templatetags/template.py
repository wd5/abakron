# -*- coding: utf-8 -*-

from django import template

register = template.Library()


class RawNode(template.Node):
    """Raw output of the django template string

    Based on the https://gist.github.com/629508
    """

    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text

@register.tag
def raw(parser, token):
    text = []

    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endraw':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append(template.base.VARIABLE_TAG_START)
        elif token.token_type == template.TOKEN_BLOCK:
            text.append(template.base.BLOCK_TAG_START)
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append(template.base.VARIABLE_TAG_END)
        elif token.token_type == template.TOKEN_BLOCK:
            text.append(template.base.VARIABLE_TAG_END)

    return RawNode(''.join(text))
