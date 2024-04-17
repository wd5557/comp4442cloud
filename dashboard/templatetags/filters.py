from django import template
register = template.Library()

@register.filter
def indexed(indexable, i):
    return indexable[i - 1]


@register.filter
def rounded(data, d=2):
    if type(data) == float:
        return round(data, d)
    else:
        return data
