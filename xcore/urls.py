from django.conf import settings
from django.conf.urls.defaults import *
from django.utils.importlib import import_module
import os
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete


media_root = settings.MEDIA_ROOT
app_media_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_media/")
maintenance_root = media_root + "/maintenance/"

_urlconf = import_module(getattr(settings, "ROOT_URLCONF"))

_urlpatterns = _urlconf.__getattribute__('urlpatterns')
_tmp_urlpatterns = []
_tmp_urlpatterns += patterns("",
                             #    (r"^app_media/(?P<path>.*)$", "django.views.static.serve", {"document_root": app_media_root, "show_indexes": False}),
                             url('^register/$', "xcore.profile.views.register", name="register"),
                             url('^login/$', login, {'template_name': 'xcore/login.html'}, name="login"),
                             url('^logout/$', logout, {'template_name': 'xcore/logout.html'}, name="logout"),
                             url('^loggedin/$', 'xcore.profile.views.loggedin'),
                             url('^accounts/profile/$', 'xcore.profile.views.profile', name="profile"),
                             #url('^set_lang/(?P<lang>.*)/$', 'xcore.utils.set_lang', name="set_lang"),
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^resetpw/$', password_reset,
         {'template_name': 'xcore/password_reset.html', 'email_template_name': 'xcore/password_reset_email.html',
          'post_reset_redirect': '/resetpw/done/'}),
    (r'^resetpw/done/$', password_reset_done, {'template_name': 'xcore/password_reset_done.html'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
         {'template_name': 'xcore/password_reset_confirm.html'}),
    (r'^reset/done/$', password_reset_complete, {'template_name': 'xcore/password_reset_complete.html'}),

                             url('^changepw/$', password_change, {'template_name': 'xcore/password_change.html'},
                                 name="change_password"),
    (r'^changepw_done/$', password_change_done, {'template_name': 'xcore/password_change_done.html'}),
    (r"^label/(?P<key>.*).png", "xcore.label.views.get_label"),
                             #    (r"^maintenance$", "django.views.static.serve", {"path": "index.html", "document_root": maintenance_root, "show_indexes": False})
                             # (r'^', include("xcore.mezz.xpages.urls"))

)

try:
    import mezzanine

    urlpatterns = _tmp_urlpatterns
except ImportError, e:
    print "here"
    _urlpatterns += _tmp_urlpatterns
