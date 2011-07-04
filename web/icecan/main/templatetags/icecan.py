
from django import template

register = template.Library()

@register.filter
def find_diff_article(needle, haystack):
    print needle
    print haystack
    match = [h for h in haystack if h['articleA'].id == needle.id]
    return None if not match else match[0]
