from django import template


register = template.Library()

@register.filter
def my_lengthrange(value, arg):
    length = len(value)
    if length <= 10:
        return (length, length+arg)
    else:
        return (length-arg, length)