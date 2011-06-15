from django import template
from django.http import HttpResponse, QueryDict
from django.utils.safestring import mark_safe
from django.core.cache import cache
from django.conf import settings
from xcore.label import textimage

import hashlib

register = template.Library()

import logging
logger = logging.getLogger("xcore.label")

@register.filter
def labelize(text="TEXT", args="black&22"):
    al = args.split("&")
    text_color = al[0]
    text_size = al[1]
    print text_color
    print text_size
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

    if cache.get(key) is None or getattr(settings, "DEBUG"):
        label = textimage.get_label(text, text_color, int(text_size))
        response = HttpResponse(label.getvalue(), mimetype="image/png")
        cache.set(key, response, 120)
        logger.info("put label to cachee")
        
    result = "<img src='/label/%s.png' />" % key
    return mark_safe(result)