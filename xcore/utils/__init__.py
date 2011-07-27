import sys
import traceback

def print_stacktrace():
    traceback.print_exc(file=sys.stdout)

def set_lang(request):
    import django.views.i18n
