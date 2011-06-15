import sys
import traceback

def print_stacktrace():
    traceback.print_exc(file=sys.stdout)
