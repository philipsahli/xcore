# Copyright (c) 2011 Philip Sahli from sahli.net

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from django.http import HttpResponseRedirect
from django.conf import settings
import logging
logger = logging.getLogger("xcore.forwarded")

class ForwardedMiddleware:
    # TODO: dok and test
    def process_request(self, request):
        forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST')
        print forwarded_host
        only_forwarded = getattr(settings, 'ONLY_FORWARDED')
        host_forwarded = getattr(settings, 'HOST_FORWARDED')
        if forwarded_host == host_forwarded or\
                only_forwarded == False:
            logger.info("received request over proxy "+str(forwarded_host)+" -> OK")
            return None
        else:
            logger.warn("received request not over proxy -> NOK")
            return HttpResponseRedirect(redirect_to='http://www1.fatrix.ch/')
