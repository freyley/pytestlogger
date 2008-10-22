import unittest
from testlogger import testlog
from StringIO import StringIO

class TestLoggerTests(unittest.TestCase):
    def setUp(self):
        testlog.reset()
        self.log = StringIO()

    def testFailuresGoToFile(self):
        testlog.log_to_file(self.log)
        testlog.assertEqual(4, 3)
        self.assertEqual(self.log.getvalue(), u'FAILED: 4 != 3 in testlogger_tests.py line 12: testlog.assertEqual(4, 3)\n')
        
    def testPassesGoToFile(self):
        testlog.log_to_file(self.log)
        testlog.logSuccesses = True
        testlog.assertEqual(4, 4)
        self.assertEqual(self.log.getvalue(),  u'PASSED: testlogger_tests.py line 18: testlog.assertEqual(4, 4)\n')

if __name__ == '__main__':
    unittest.main()
