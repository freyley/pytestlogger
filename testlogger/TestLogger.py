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


    def __assertEqual(self,  first,  second,  msg=None):
        def func():
            super(TestLogger,  self).assertEqual(first,  second,  msg)
        self.logAssert(func)
            
    #def assertAlmostEqual(self):
    #    pass
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
