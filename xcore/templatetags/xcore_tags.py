from django import template
from django.template.loader import get_template

register = template.Library()

import logging
logger = logging.getLogger("xcore")

@register.inclusion_tag("xcore_head.html", takes_context=True)
def xcore_head(context):
    """
    Set up the required JS/CSS for the in-line editing toolbar and controls.
    """
    t = get_template("xcore_head.html")
    return context


def default_if_empty(value, arg):
    """Returns a boolean of whether the value's length is the argument."""
    if len(value)>0:
        return value
    return arg
#    try:
#        return len(value) == int(arg)
#    except (ValueError, TypeError):
#        return ''
default_if_empty.is_safe = False
register.filter(default_if_empty)