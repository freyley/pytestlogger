import unittest
import exceptions
import inspect

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
        codeline = stack[2][1] + ' line ' + str(stack[2][2]) + ': ' + stack[2][4][0].strip()
        return codeline

    def logAssert(self,  assertCall):
        try:
            assertCall()
            if self.logSuccesses:
                codeline = self.reportLine(inspect.stack())
                self.logger('PASSED: ' + codeline)
        except exceptions.AssertionError,  ae:
            codeline = self.reportLine(inspect.stack())
            self.logger('FAILED: ' + ae.message + ' in ' + codeline)

    def foo(self,  method):
        class_ = method.im_class
        name_ = method.__name__
        def alias_method(*args,  **kwargs):
            print 'whatup?'
            retval = method(*args,  **kwargs)
            return retval
        setattr(class_,  name_,  alias_method)

    def assertEqual(self,  first,  second,  msg=None):
        def func():
            super(TestLogger,  self).assertEqual(first,  second,  msg)
        self.logAssert(func)
            
    def assertAlmostEqual(self):
        pass
'''        
 'assertAlmostEquals',
 'assertEqual',
 'assertEquals',
 'assertFalse',
 'assertNotAlmostEqual',
 'assertNotAlmostEquals',
 'assertNotEqual',
 'assertNotEquals',
 'assertRaises',
 'assertTrue',
 'assert_',
'fail',
 'failIf',
 'failIfAlmostEqual',
 'failIfEqual',
 'failUnless',
 'failUnlessAlmostEqual',
 'failUnlessEqual',
 'failUnlessRaises',
 'failureException',
 #function.func_code.co_varnames gets the argument names

'''
