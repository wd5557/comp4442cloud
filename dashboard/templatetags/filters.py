from django import template
register = template.Library()

@register.filter
def indexed(indexable, i):
    return indexable[i - 1]