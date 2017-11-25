from django import template

register = template.Library()


@register.simple_tag(name='multiply')
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    a = qty * unit_price
    a = format(a, '.2f')
    return a

