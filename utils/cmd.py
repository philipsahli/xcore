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

from subprocess import Popen
import subprocess, os


class Command():
    def __init__(self, arg):
        self.arg = arg


class Executor():
    @staticmethod
    def execute(cmd, communicate=False, return_pid=False):
        print cmd.arg
        p = Popen(cmd.arg, shell=return_pid, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if communicate:
            return p.communicate()
        elif return_pid:
            print p.pid
            return p.pid
        else:
            p.wait()
        if p.returncode == 0:
            return True
        elif p.returncode == 1:
            return False

class Starter():
    @staticmethod
    def go(app):
        pid = Executor.execute(Command(app.command.split(" ")), return_pid=True)
        return pid

    @staticmethod
    def back(app):
        os.kill(app.pid)
        return True

