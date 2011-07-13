'''
Created on Jan 22, 2011
'''

from django.core.cache import cache
from django.http import Http404
import logging

logger = logging.getLogger("xcore")

def get_label(request, key):
    logger.info("get label")
    print "get label"
    try: 
        response = cache.get(key)
        if response == None:
            raise Http404
        else:
            logger.info("get label from cache")
    except Exception, e:
        logger.info(e)
        print e
    return response