import unittest
from testlogger import testlog
from StringIO import StringIO
import inspect,  sys

class TestLoggerTests(unittest.TestCase):
    def setUp(self):
        testlog.reset()
        self.log = StringIO()
        testlog.log_to_file(self.log)

    def testFailuresGoToFile(self):
        testlog.assertEqual(4, 3)
        answer = u'FAILED: 4 != 3 in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+ ': testlog.assertEqual(4, 3)\n'
        self.assertEqual(self.log.getvalue(), answer)
        
    def testPassesGoToFile(self):
        testlog.logSuccesses = True
        testlog.assertEqual(4, 4)
        answer = u'PASSED: testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+': testlog.assertEqual(4, 4)\n'
        self.assertEqual(self.log.getvalue(),  answer)
        testlog.assertEqual(4, 3)
        answer += u'FAILED: 4 != 3 in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+ ': testlog.assertEqual(4, 3)\n'
        self.assertEqual(self.log.getvalue(), answer)
        

    def testAllFunctions(self):
        testlog.assertTrue(1 == 2)
        answer = u'FAILED:  in testlogger_tests.py line '+str(inspect.getlineno(sys._getframe()) -1)+': testlog.assertTrue(1 == 2)\n'
        self.assertEqual(self.log.getvalue(),  answer)

if __name__ == '__main__':
    unittest.main()
