=============
What is Xcore
=============
Xcore is a collection of helper apps, middlewares and more for Django.


Label App
=========
Create titles on your website as images in png-format with shipped or your own fonts.

Features:

 * label get cached when template gets rendered, if caching is enabled (strongly recommended)
 * supports HTTP 302 with etag and last-modified HTTPHeaders

Included fonts:

 * Some fonts are included, taken from:
    - http://www.dafont.com
    - http://openfontlibrary.org/

 * License included if provided by the creator.

Usage::

 {% load label_tags %}
 ...
 <h1>{{ 'My Title'|labelize:"class=default" }}</h1>
 <h1>{{ 'My Title'|labelize:"color=#DF1F72&font=Futura Md BT Bold" }}</h4>

Configuration
-------------
Place your fontfiles (ttf or otf format) in XCORE_FONTS_DIR:

settings.py::

 XCORE_FONTS_DIR = [os.path.join(projectdir, "fonts_dir")]

Configure a class with font name (as defined in fontfile), size and color:

::

 XCORE_LABELCONFIG = {
    'default': {
        'font': "Caviar Dreams Bold",
         'size': "22",
         'color': "#DF1F72",
    }
 }

Management command
------------------

 ::

Output of all font-files which are recognized.

Middlewares
===========

EmailOnNotFoundMiddleware
-------------------------
xcore.forwarded.middleware.ForwardedMiddleware

Sends an email to the admin if a HttpResponseNotFound happens (if settings.DEBUG is false).


ForwardedMiddleware
-------------------
 xcore.forwarded.middleware.ForwardedMiddleware

If a django webapp should be reached only proxied by another server, you can activate this middleware.

Configuration:

* settings.ONLY_FORWARDED (true or false)
* settings.HOST_FORWARDED (Host which must be in HTTP_X_FORWARDED_HOST Header-Field)
* settings.REDIRECT_FORWARDED (URL to redirect to with a HttpRedirectResponse)

MaintenanceMiddleware
---------------------
 xcore.maintenance.middleware.MaintenanceMiddleware

If settings.MAINTENANCE_ON is True, a HttpResponseServiceUnavailable (Response-Code 503) is returned.
The paths for admin and __debug__ are excluded for this functionality, therefore in maintenance mode the admin
can still login into Django Admin and the HTML-File which can be displayed is available under the
URL '/media/maintenance/index.html'

In Mezzanine the setting is registered as editable setting in the admin.


XPages for Mezzanine
====================
XPages xcore.mezz.xpages.models.XPage
