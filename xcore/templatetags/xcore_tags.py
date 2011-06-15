from django import template
from django.template.loader import get_template
from django.http import HttpResponse
from xcore.utils import textimage
from django.utils.safestring import mark_safe

from django.core.cache import cache

from django.conf import settings

import hashlib

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
