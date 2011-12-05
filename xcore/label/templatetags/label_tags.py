from django import template
from django.http import HttpResponse, QueryDict
from django.utils.safestring import mark_safe
from django.core.cache import cache
from django.conf import settings
from xcore.label import textimage
import hashlib
from datetime import datetime
from xcore.utils.profiler import profile

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


    # resolve transation
    text = unicode(text)

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
    key = "xcore.label."+calculate_key(text, text_size, text_font, text_color)

    cached = get_label_by_key(key)
    if not cached:
        logger.debug("going to create label "+_debug_key(key, text))
        text = text.encode("iso8859-1")
        label = textimage.get_label(text, text_color, int(text_size), text_font)
        _cache_label(key, label)

    return _create_imgtag(key), cached, key

def get_label_by_key(key, exists=False):
    if not cache.get(key):
        return False
    return True

def calculate_key(*args):
    m = hashlib.md5()
    m.update(args[0])
    m.update(args[1])
    m.update(args[2])
    return  m.hexdigest()

def _create_imgtag(key):
    result = "<img src='/label/%s.png' alt='%s'/>" % (key, key)
    return mark_safe(result)

def _cache_label(key, label):
    frmt = "%d %b %Y %H:%M:%S %Z"
    d = datetime.now()

    etag = hashlib.md5()
    etag.update(key)
    etag.update(d.strftime(frmt))
    s_etag = str(etag.hexdigest())

    v = {
        'last_modified': d.now(),
        'label': label,
        'etag': s_etag
    }

    try:
        cache_seconds = settings.CACHES['default']['TIMEOUT']
    except KeyError:
        cache_seconds = 1500
    logger.debug("cached for "+str(cache_seconds)+"s: "+key)
    cache.set(key, v, cache_seconds)

def _debug_key(key, text):
    return key+" ("+str(text)+")"
