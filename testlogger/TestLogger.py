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
        if stack[2][4]:
            codeline = stack[2][1] + ' line ' + str(stack[2][2]) + ': ' + stack[2][4][0].strip()
        else:
            codeline = ' console'
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

    def assertEqual(self,  first,  second,  msg=None):
        def func():
            super(TestLogger,  self).assertEqual(first,  second,  msg)
        self.logAssert(func)
            
    def assertAlmostEqual(self,  first,  second,  places=6,  msg=None):
        def func():
            super(TestLogger,  self).assertAlmostEqual(first,  second,  places,  msg)
        self.logAssert(func)
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
