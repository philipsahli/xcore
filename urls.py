from django.conf import settings
import os

media_root = settings.MEDIA_ROOT
app_media_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_media/")
maintenance_root = media_root+"/maintenance/"

#_urlconf = import_module(getattr(settings, "ROOT_URLCONF"))
#_urlpatterns = _urlconf.__getattribute__('urlpatterns')

#_urlpatterns += patterns("",
#    (r"^app_media/(?P<path>.*)$", "django.views.static.serve", {"document_root": app_media_root, "show_indexes": False}),
#    (r"^register$", "xcore.profile.views.register"),
#    (r"^label/(?P<key>.*).png", "xcore.label.views.get_label"),
#    (r"^maintenance$", "django.views.static.serve", {"path": "index.html", "document_root": maintenance_root, "show_indexes": False})
#)