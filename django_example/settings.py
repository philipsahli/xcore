# Django settings for django_example project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Philip Sahli', 'ilipcito@gmail.com')
)

# add xcore module to path
import sys
sys.path.append("..")
projectdir = os.path.abspath(os.getcwd())

# AUTH_PROFILE_MODULE - could go to xcore module
AUTH_PROFILE_MODULE = 'profile.UserProfile'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ilipcito@gmail.com'
EMAIL_HOST_PASSWORD = 'winston2'
EMAIL_PORT = 587

MAINTENANCE_ON=False

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_example.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(projectdir, "media")
print MEDIA_ROOT

MEDIA_URL = "/media"

STATIC_ROOT = os.path.join(projectdir, "static")
STATIC_URL = "/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w$+j_ogl(ojqt1t-2h!8_xepm+#+#+6410_02*&592wycjg42*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'xcore.maintenance.middleware.MaintenanceMiddleware',
    'xcore.forwarded.middleware.ForwardedMiddleware',
    'xcore.common.middleware.EmailOnNotFoundMiddleware',
)

ROOT_URLCONF = 'django_example.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(projectdir, "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'south',
    'xcore',
    'xcore.i18n',
    'xcore.label',
    'xcore.profile',
    'xcore.maintenance',
    'debug_toolbar'
)
LANGUAGES = ("en", "de")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
         'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'class':  'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'simple', 
            'filename': 'django_example.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            #'filters': ['special']
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'xcore': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        }
    }
}

ONLY_FORWARDED = False
HOST_FORWARDED = "asdf"
REDIRECT_FORWARDED = "http://127.0.0.1:8000"

INTERNAL_IPS = ('127.0.0.1')

XCORE_FONTS_DIR = [os.path.join(projectdir, "fonts_dir")]
XCORE_LABELCONFIG = {
    'default': {
        'font': "Caviar Dreams Bold",
        'size': "22",
        'color': "#DF1F72",
        #'color': "black",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
