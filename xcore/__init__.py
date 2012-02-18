# Activate urls
__version__ = "0.12b"
import os

# fix for xcore, hook urls only when django env is set
django_settings = os.environ.get('DJANGO_SETTINGS_MODULE')
if django_settings is not None:
    import urls


#def show_urls(urllist, depth=0):
#    for entry in urllist:
#        print "  " * depth, entry.regex.pattern
#        if hasattr(entry, 'url_patterns'):
#            show_urls(entry.url_patterns, depth + 1)
#
#show_urls(urls.urlpatterns)