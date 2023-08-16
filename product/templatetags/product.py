from django import template
register = template.Library()


@register.filter
def format_price(price):
    return '{:,}'.format(price).replace(',', ' ')