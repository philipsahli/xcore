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

from mezzanine.pages.models import  Page
from mezzanine.core.fields import HtmlField
from mezzanine.core.models import RichText
from django.db.models import ImageField
from django.db import models
from django.utils.translation import ugettext_lazy as _

class XPage(Page, RichText):
    splash_text = HtmlField(_("Splash"), null=True, blank=True)
    splash_image = ImageField("Image", upload_to="splash/", blank=True, null=True)
    with_splash = models.BooleanField(default=True)

    class Meta:
       verbose_name = _("XPage")
       verbose_name_plural = _("XPages")

#    @models.permalink
#    def get_absolute_url(self):
#        return ("page", (), {"slug": self.get_slug()})

    def get_splash_image(self):
        if not self.splash_image.name:
            return "No splash image"
        return "<img width='50px' class='img_block' src='%s'/>" % self.splash_image.url

    def is_published(self):
        return (self in Page.objects.published())
