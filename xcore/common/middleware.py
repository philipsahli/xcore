__author__ = 'fatrix'
from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponseNotFound
from django.conf import settings
import logging
import pprint

logger = logging.getLogger("xcore")

class EmailOnNotFoundMiddleware(object):
    def __init__(self):
        if not settings.DEBUG:
            raise MiddlewareNotUsed()

    def process_response(self, request, response):
        pp = pprint.PrettyPrinter(indent=4)
        #if isinstance(response, HttpResponseNotFound):
        #    logging.error(pp.pprint(response.__dict__))
        return response
  
