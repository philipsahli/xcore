from django import template
from django.http import HttpResponse, QueryDict
from django.utils.safestring import mark_safe
from django.core.cache import cache
from django.conf import settings
from xcore.label import textimage
import hashlib

register = template.Library()

import logging
logger = logging.getLogger("xcore")

@register.filter
def labelize(text, args):
    """
    Create the label and put it in the cache.
    Return an img-tag to retrieve it with a a view.
    """
    qs = QueryDict(args)

    text_size = qs.get('size')
    text_color = qs.get('color')
    text_font = qs.get('font')

    text_class = qs.get('class', "default")

    #if (not text_size and not text_color and not text_font) or (not text_class):
    #    raise Exception("configuration error in labelconfig, cannot labelize '%s'" % text)

    labelconfig = getattr(settings, "XCORE_LABELCONFIG")

    if not text_size:
        text_size = labelconfig[text_class]['size']
    if not text_font:
        text_font = labelconfig[text_class]['font']
    if not text_color:
        text_color = labelconfig[text_class]['color']

    tag, cached, key = handle_rendering(text, text_size, text_font, text_color)
    logger.debug("handling "+_debug_key(key, text) +" cached: "+str(cached))
    return tag

def handle_rendering(text, text_size, text_font, text_color):
    key = "xcore.label."+calculate_key(str(text), text_size, text_font, text_color)

    cached = get_label_by_key(key)
    if not cached:
        text = text.encode("iso8859-1")
        label = textimage.get_label(text, text_color, int(text_size), text_font)
        response = HttpResponse(label.getvalue(), mimetype="image/png")
        _cache_label(key, response)

    return _create_imgtag(key), cached, key

def get_label_by_key(key, exists=False):
    if cache.get(key) is None or getattr(settings, "DEBUG"):
        exists = False
    return exists

def calculate_key(*args):
    m = hashlib.md5()
    m.update(args[0])
    m.update(args[1])
    m.update(args[2])
    return  m.hexdigest()

def _create_imgtag(key):
    result = "<img src='/label/%s.png' alt='%s'/>" % (key, key)
    return mark_safe(result)

def _cache_label(key, response):
    try:
        cache_seconds = settings.CACHES['default']['TIMEOUT']
    except KeyError:
        cache_seconds = 120
    cache.set(key, response, cache_seconds )

def _debug_key(key, text):
    return key+" ("+text+")"

