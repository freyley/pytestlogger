import unittest
import exceptions
import inspect
import sys

class TestLogger(unittest.TestCase):
    def runTest(self):
        '''This TestCase logs errors in running code'''
        pass

    def logger(self,  report):
        print "No logger defined. This shouldn't happen."

    def reset(self):
        self.logSuccesses = False
        def stderrlogger(report):
            sys.stderr.writelines(report)
        self.logger = stderrlogger
    
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

    def fail(self, msg=None):
        def func():
            super(TestLogger,  self).fail( msg)
        self.logAssert(func)

    def failIf(self, expr, msg=None):
        def func():
            super(TestLogger,  self).failIf(expr,  msg)
        self.logAssert(func)

    def failUnless(self, expr, msg=None):
        def func():
            super(TestLogger,  self).failUnless(self,  expr,  msg)
        self.logAssert(func)

    def failUnlessRaises(self, excClass, callableObj, *args, **kwargs):
        def func():
            super(TestLogger,  self).failUnlessRaises(excClass,  callableObj,  *args,  **kwargs)
        self.logAssert(func)

    def failUnlessEqual(self, first, second, msg=None):
        def func():
            super(TestLogger,  self).failUnlessEqual(first,  second,  msg)
        self.logAssert(func)

    def failIfEqual(self, first, second, msg=None):
        def func():
            super(TestLogger,  self).failIfEqual(first,  second,  msg)
        self.logAssert(func)

    def failUnlessAlmostEqual(self, first, second, places=7, msg=None):
        def func():
            super(TestLogger,  self).failUnlessAlmostEqual(first,  second,  places,  msg)
        self.logAssert(func)

    def failIfAlmostEqual(self, first, second, places=7, msg=None):
        def func():
            super(TestLogger,  self).failIfAlmostEqual(first,  second,  places,  msg)
        self.logAssert(func)
    # Synonyms for assertion methods

    assertEqual = assertEquals = failUnlessEqual

    assertNotEqual = assertNotEquals = failIfEqual

    assertAlmostEqual = assertAlmostEquals = failUnlessAlmostEqual

    assertNotAlmostEqual = assertNotAlmostEquals = failIfAlmostEqual

    assertRaises = failUnlessRaises

    assert_ = assertTrue = failUnless

    assertFalse = failIf
