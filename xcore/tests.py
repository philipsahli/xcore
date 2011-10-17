from django.test import TestCase
import os
from label.textimage import get_label
from django.test.client import Client

from django.contrib.auth.models import User
from profile.models import UserProfile

from django.conf import settings
from maintenance.middleware import MaintenanceMiddleware
from maintenance.utils import create_maintenance_file
from xcore.label.templatetags.label_tags import handle_rendering

import logging
logging.disable(logging.DEBUG)
logging.disable(logging.ERROR)

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

class LabelTest(TestCase):

    def test_get_label(self):
        label = get_label(text="HalloWelt")
        self.assertEquals("StringO", label.__class__.__name__)

    def test_template_tag(self):
        from xcore.label.templatetags.label_tags import labelize
        self.assertEquals("<img src='/label/dfa44caf24f48564be2e034ba6d792ed.png' />", labelize("ASDF", "class=default"))

    def test_direct_label(self):
        imgtag, cached, key = handle_rendering("ASDF", "22", "GeosansLight", "black")
        self.assertEqual("<img src='/label/702bfb96c014593f592195db9bda45ee.png' />", imgtag)
        self.assertEqual(cached, False)

    def test_get_label_not_in_cache(self):
        c = Client()
        response = c.get("/label/asdf.png")
        self.assertEquals(404, response.status_code)
