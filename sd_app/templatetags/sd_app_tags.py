from django import template
register = template.Library()

@register.simple_tag
def calculate_price(gallons_requested, suggested_price):
    return gallons_requested * suggested_price