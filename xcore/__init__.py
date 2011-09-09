# Activate urls
__version__ = "0.12"
import os

# fix for xcore, hook urls only when django env is set
django_settings = os.environ.get('DJANGO_SETTINGS_MODULE')
if django_settings is not None:
    import urls
