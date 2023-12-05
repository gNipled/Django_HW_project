from django import template


register = template.Library()


@register.filter()
def mymedia(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.simple_tag
def mediapath(path):
    if path:
        return f'/media/{path}'
    return '#'
