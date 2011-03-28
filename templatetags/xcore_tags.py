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

@register.filter
def labelize(text="TEXT"):
    # TODO: Should receive font family and size as arg
    """
    Create the label and put it in the cache.
    Return an img-tag to retrieve it with a a view.
    """
    text = text.encode("iso8859-1")
    m = hashlib.md5()
    m.update(text)
    m.update(text)
    key =  m.hexdigest()

    if cache.get(key) == None or getattr(settings, "DEBUG"):
        label = textimage.get_label(text)
        response = HttpResponse(label.getvalue(), mimetype="image/png")
        cache.set(key, response, 120)
        logger.info("put label to cachee")
        
    result = "<img src='/label/%s.png' />" % key
    return mark_safe(result)
