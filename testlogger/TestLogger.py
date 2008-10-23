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
        print "%s %s srated" % (class_.__name__, name_)
        retval = method(*args, **kwargs)
        print "%s %s finished" % (class_.__name__, name_)
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

filterfunc = lambda x: ((x.startswith('assert') or x.startswith('fail')) and not x.endswith('Exception'))
functions = filter(filterfunc,  dir(TestLogger))
for funcname in functions:
    func = getattr(TestLogger,  funcname)
    trace_it(func,  funcname)

