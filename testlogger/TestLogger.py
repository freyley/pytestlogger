import unittest
import exceptions
import inspect

class TestLogger(unittest.TestCase):
    def runTest(self):
        pass
    def __init__(self):
        filterfunc = lambda x: ((x.startswith('assert') or x.startswith('fail')) and not x.endswith('Exception'))
        for func in filter(filterfunc,  dir(self)):
            func = getattr(self,  func)
            def method(*args,  **kwargs):
                print 'beginning'
                retval = func(*args,  **kwargs)
                print 'ending'
                return retval
            setattr(self,  func.__name__,  method)

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
