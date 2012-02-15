from django.core.mail import mail_admins
from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponseNotFound
from django.conf import settings

class EmailOnNotFoundMiddleware(object):
    def __init__(self):
        if settings.DEBUG:
            raise MiddlewareNotUsed()

    def process_response(self, request, response):
        if isinstance(response, HttpResponseNotFound):
            if request.path != '/favicon.ico':
                mail_admins("404 happend on URL %s" % request.path, "pp.pprint(request.__dict__")
        return response
  
