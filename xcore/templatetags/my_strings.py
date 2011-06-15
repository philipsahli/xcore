from django import template
register = template.Library()

@register.filter
def replace(value):
    valueNew = str(value).replace("_"," ")
    return valueNew
