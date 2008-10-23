import unittest
import exceptions
import inspect
import datetime

def wrap_method(method,  methodname):
    # retrieve the enclosing class of the method
    class_ = method.im_class
    # retrieve the method name
    name_ = methodname

    def alias_method(*args, **kwargs):
        retval = None
        try:
            retval = method(*args, **kwargs)
            if self.logSuccesses:
                codeline = self.reportLine(inspect.stack())
                self.logger('PASSED: ' + codeline)
        except exceptions.AssertionError,  ae:
            codeline = self.reportLine(inspect.stack())
            self.logger('FAILED: ' + ae.message + ' in ' + codeline)
        finally:
            return retval

    # replace the original method with the alias
    setattr(class_, name_, alias_method)


class TestLogger(unittest.TestCase):
    def runTest(self):
        pass
        
    def logger(self,  report):
        print "No logger defined. This shouldn't happen."

    def reset(self):
        self.logSuccesses = False
        def printlogger(report):
            print report
        self.logger = printlogger
    
    def log_to_file(self, fp):
        def filelogger(report):
            fp.write(report + u'\n')
        self.logger = filelogger

    def reportLine(self,  stack):
        if stack[2][4]:
            codeline = stack[2][1] + ' line ' + str(stack[2][2]) + ': ' + stack[2][4][0].strip()
        else:
            codeline = ' console'
        return codeline

filterfunc = lambda x: ((x.startswith('assert') or x.startswith('fail')) and not x.endswith('Exception'))
functions = filter(filterfunc,  dir(TestLogger))
for funcname in functions:
    func = getattr(TestLogger,  funcname)
    wrap_method(func,  funcname)
