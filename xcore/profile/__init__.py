# TODO: add urls to __init__

from django.conf.urls.defaults import *

urlpatterns = patterns("",
     (r"^register$", "xcore.profile.views.register"),
)

