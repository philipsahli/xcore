'''
Created on Jan 22, 2011
'''

from django.core.cache import cache
from django.http import Http404, HttpResponseServerError, HttpResponseNotFound, HttpResponseNotModified
import logging


logger = logging.getLogger("xcore")


def get_label(request, key):
    if_modified_since = request.META.get('HTTP_IF_MODIFIED_SINCE')
    if if_modified_since:
        return HttpResponseNotModified()
    try:
        response = cache.get(key)
        if not response:
            logger.error("label %s not found in cache" % key)
            return HttpResponseNotFound()
        else:
            logger.info("get label %s from cache" % key)
    except Exception, e:
        logger.error(e.__class__)
        return HttpResponseServerError()
    return response