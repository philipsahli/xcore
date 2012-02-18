from django.conf import settings
from django.conf.urls.defaults import *
from django.utils.importlib import import_module
import os


media_root = settings.MEDIA_ROOT
app_media_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_media/")
maintenance_root = media_root + "/maintenance/"

_urlconf = import_module(getattr(settings, "ROOT_URLCONF"))

_urlpatterns = _urlconf.__getattribute__('urlpatterns')
_tmp_urlpatterns = []
_urlpatterns += patterns("",
    (r"^label/(?P<key>.*).png", "xcore.label.views.get_label"),
)

#try:
#    import mezzanine
_urlconf.urlpatterns += _tmp_urlpatterns
urlpatterns = _tmp_urlpatterns
#except ImportError, e:
#    _urlpatterns += _tmp_urlpatterns

#for pattern in _urlpatterns:
#    print pattern
#import urls
#
#def show_urls(urllist, depth=0):
#    for entry in urllist:
#        print "  " * depth, entry.regex.pattern
#        if hasattr(entry, 'url_patterns'):
#            show_urls(entry.url_patterns, depth + 1)
#
#show_urls(urls._urlpatterns)
