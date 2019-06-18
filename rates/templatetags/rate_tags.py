from django import template

register = template.Library()

def add_number(value, addition):
    value = int(value) + int(addition)
    return value

register.filter('add_number', add_number)
