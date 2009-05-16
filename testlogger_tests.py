import unittest
from testlogger import testlog
from StringIO import StringIO
import inspect,  sys
import logging

class TestLoggerTests(unittest.TestCase):
    def setUp(self):
        testlog.reset()
        self.log = StringIO()
	self.log.name = 'StringIO for Testing'
        testlog.log_to_file(self.log)

    def testFailuresGoToFile(self):
        testlog.assertEqual(4, 3)
        answer = u'FAILED: 4 != 3 in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+ ': testlog.assertEqual(4, 3)\n'
        self.assertEqual(self.log.getvalue()[28:], answer)
        
    def testPassesGoToFile(self):
        testlog.logSuccesses = True
        testlog.assertEqual(4, 4)
        answer = u'PASSED: testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+': testlog.assertEqual(4, 4)\n'
        self.assertEqual(self.log.getvalue()[28:],  answer)
        testlog.assertEqual(4, 3)
        answer = u'FAILED: 4 != 3 in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+ ': testlog.assertEqual(4, 3)\n'
        self.assertEqual(self.log.getvalue()[119:], answer)

    def testAllFunctions(self):
        testlog.assertTrue(1 == 2)
        answer = u'FAILED:  in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+': testlog.assertTrue(1 == 2)\n'
        self.assertEqual(self.log.getvalue()[28:],  answer)

    def testLoggingToLogging(self):
        testlog.log_to_logging(logging)
        testlog.assertTrue(4, 3)
        # TODO: ascertain that it went to logging
    
    def testSetVerboseErrorsWhenNotBoolean(self):
        testlog.set_verbose(4)
        answer = u'FAILED: testlog.set_verbose takes True or False, not 4'
        self.assert_(self.log.getvalue()[28:].startswith(answer))
    
    def testSetVerboseIncreasesVerbosity(self):
        testlog.set_verbose(True)
        # TODO: so what does this look like?    

if __name__ == '__main__':
    unittest.main()
