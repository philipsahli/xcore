from django.core.management.base import BaseCommand
from xcore.label import textimage

__author__ = 'fatrix'

class Command(BaseCommand):
    def handle(self, *args, **options):
        for font in textimage.fonts.__iter__():
            print "    "+str(textimage.fonts.get(font))

  