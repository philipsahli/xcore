from django.test import TestCase
import os
from label.textimage import get_label
from django.test.client import Client

from django.contrib.auth.models import User
from profile.models import UserProfile

from django.conf import settings
from maintenance.middleware import MaintenanceMiddleware
from maintenance.utils import create_maintenance_file
from xcore.label.templatetags.label_tags import labelize, handle_rendering, IMG_TAG

import logging
logging.disable(logging.DEBUG)
logging.disable(logging.WARN)
logging.disable(logging.ERROR)

TEXT = "ASDF"
KEY = "xcore.label.e04dd8c26c64a4756fc3eda2e619d1de"

class RegisterTest(TestCase):
    
    url = "/register/"
    c = None
    user = None
    profile = None

    def setUp(self):
        self.c = Client()
        
    def tearDown(self):
        try:
            self.user.delete()
            self.profile.delete()
        except Exception, e:
            pass

    def testRegister(self):

        response = self.c.get(self.url, follow=True)
        self.assertEquals(200, response.status_code)

        new_user = User.objects.create_user(username="asdf",
                                            email="asdf@asdf.com",
                                            password="blablabla")
        self.assertEquals(1, new_user.id)
        up = UserProfile(user=new_user, url="", country="", email=new_user.email)
        up.save()
        self.assertEquals(1, up.id)

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

from xcore.label.tests import *
