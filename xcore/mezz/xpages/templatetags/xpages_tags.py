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


from django import template
import django
from xcore.mezz.xpages.models import XPage
from django.template.loader import get_template
from django.template import Context

register = template.Library()

def splash_list(context):
    request = context['request']
    page_branch = context['page_branch']
    xpages = []
    anon = (request.user.__class__==django.contrib.auth.models.AnonymousUser)
    for page in page_branch:
        try:
            page.is_published = page.get_content_model().is_published()
            if anon:
                pass
            else:
                print "addd"
                xpages.append(page.get_content_model())
        except:
            pass

    t = get_template("xpages/splash_list.html")
    return t.render(Context({"xpages": xpages}))

register.simple_tag(splash_list, takes_context=True)
