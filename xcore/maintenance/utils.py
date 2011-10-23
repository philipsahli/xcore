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

from django.conf import settings
from django.template.context import RequestContext

from django.template.loader import render_to_string
from django.template import Context
import logging
logger = logging.getLogger(name="xcore")

def create_maintenance_file():
    media_root = getattr(settings, "MEDIA_ROOT")
    try:
        c = Context({"MEDIA_URL": settings.MEDIA_URL})
        # TODO: Fix RequestContext
        rendered = render_to_string('maintenance.html', context_instance=c)
        fp = media_root + "/maintenance/index.html"
        file = open(fp, "w")
        file.write(rendered.encode('utf-8'))
        file.close()
    except Exception, e:
        logger.error(e.message)
        return False, None
    return True, fp