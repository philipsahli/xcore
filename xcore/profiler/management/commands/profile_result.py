from django.core.management.base import BaseCommand

__author__ = 'fatrix'


class Command(BaseCommand):
    def handle(self, *args, **options):
        from xcore.profiler import profile_result
        profile_result()

  