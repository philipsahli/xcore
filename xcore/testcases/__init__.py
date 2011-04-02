# Copyright (c) 2011 Philip Sahli from sahli.net

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import unittest, time, os
from selenium import selenium
from xcore.utils.cmd import Executor, Command

class SeleniumTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', dir = '.'):
        self.dir = dir
        super(SeleniumTestCase, self).__init__(methodName)

    def setUp(self):
        self.verificationErrors = []
        self.startSeleniumServer()
        self.startDjango()
        self.selenium = selenium("localhost", 4444, "*firefox", "http://127.0.0.1:8888")
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()
        self.stopSeleniumServer()
        self.stopDjango()
        self.assertEqual([], self.verificationErrors)

    def startSeleniumServer(self):
        # TODO: fix path to selenium.jar
        self.selenium_pid = Executor.execute(Command(["java", "-jar", "/Users/fatrix/Downloads/selenium-server-standalone-2.0b3.jar"]), background=True)
        time.sleep(10)

    def stopSeleniumServer(self):
        Executor.execute(Command(["kill", "-9", "%s" % self.selenium_pid]))

    def stopDjango(self):
        Executor.execute(Command(["kill", "-9", "%s" % self.django_pid]))
        Executor.execute(Command(["kill", "-9", "%s" % str(int(self.django_pid)+1)]))

    def startDjango(self):
        self.django_pid = Executor.execute(Command(["python", os.path.join(self.dir, "manage.py"), "runserver", "127.0.0.1:8888"]), background=True)
        time.sleep(1)