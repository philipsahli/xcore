from django.test import TestCase
import os
from django.test.client import Client
from django.core import mail
from django.conf import settings
from maintenance.middleware import MaintenanceMiddleware
from maintenance.utils import create_maintenance_file

import logging
logging.disable(logging.DEBUG)
logging.disable(logging.WARN)
logging.disable(logging.ERROR)

TEXT = "ASDF"
KEY = "xcore.label.e04dd8c26c64a4756fc3eda2e619d1de"

class MaintenanceTest(TestCase):

    c = None

    def setUp(self):

        self.c = Client()

    def tearDown(self):
        try:
            self.user.delete()
            self.profile.delete()
        except Exception, e:
            pass
        
    def testMaintenance_should_end_in_redirection(self):
        response = self.c.get("/")
        self.assertEquals(200, response.status_code)

        setattr(settings, MaintenanceMiddleware.setting, True)
        response = self.c.get("/")
        self.assertEquals(503, response.status_code)

        response = self.c.get("/admin")
        self.assertEquals(301, response.status_code)

        setattr(settings, MaintenanceMiddleware.setting, False)


    def testStaticMaintenanceFile_should_generate(self):
        created, file_path = create_maintenance_file()
        self.assertTrue(True, created)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)


class EmailOnNotFoundTest(TestCase):

    def testMail_is_sent(self):
        c = Client()
        settings.DEBUG = False
        response = c.get("/doesnexist/")
        self.assertEquals(404, response.status_code)
        self.assertEquals(len(mail.outbox), 1)
