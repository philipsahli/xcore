from django.test import TestCase
from django.test.client import Client
from xcore.label.templatetags.label_tags import labelize, handle_rendering
from xcore.label.textimage import get_label

import logging

logging.disable(logging.DEBUG)
logging.disable(logging.WARN)
logging.disable(logging.ERROR)

TEXT = "ASDF"
KEY = "xcore.label.e04dd8c26c64a4756fc3eda2e619d1de"

class LabelTest(TestCase):

    def test_get_label(self):
        label = get_label(text="HalloWelt")
        self.assertEquals("tuple", label.__class__.__name__)

    def test_template_tag(self):
        self.assertTrue('img' in labelize(TEXT, "class=default"))

    def test_direct_label(self):
        imgtag, cached, key = handle_rendering("ASDF", "22", "GeosansLight Regular", "black")
        self.assertTrue('img' in imgtag)

    def test_get_label_not_in_cache(self):
        c = Client()
        response = c.get("/label/asdf.png")
        self.assertEquals(404, response.status_code)


