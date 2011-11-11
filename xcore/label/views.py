'''
Created on Jan 22, 2011
'''

from django.core.cache import cache
from django.views.decorators.http import condition
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseNotFound, HttpResponseNotModified
import logging
import datetime


logger = logging.getLogger("xcore")


# return date
def last_modified(request, key):
    return cache.get(key)['last_modified']

# return etag
def etag(request, key):
    return cache.get(key)['etag']

@condition(etag_func=etag, last_modified_func=last_modified)
def get_label(request, key):
    try:
        v = cache.get(key)
        if not v:
            logger.error("label %s not found in cache" % key)
            return HttpResponseNotFound()
        else:
            logger.info("get label %s from cache" % key)
    except Exception, e:
        logger.error(e.__class__)
        logger.error(e.message)
        return HttpResponseServerError()
    response = HttpResponse(v['label'].getvalue(), mimetype="image/png")
    frmt = "%d %b %Y %H:%M:%S %Z"
    expires = datetime.datetime.today() +datetime.timedelta(30)
    response['Expires'] = expires.strftime(frmt)
    return response


