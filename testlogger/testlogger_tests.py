import unittest
from testlogger import testlog
from StringIO import StringIO

class TestLoggerTests(unittest.TestCase):
    def setUp(self):
        testlog.reset()
        self.log = StringIO()

    def testFailuresGoToFile(self):
        testlog.log_to_file(self.log)
        testlog.assert_(False)
        self.assertEqual(self.log.getvalue(), 'FAILED: testlog.assert_(False)')
        
    def testPassesGoToFile(selfself):
        testlog.log_to_file(self.log)
        testlog.assertEqual(4,  4)
        self.assertEqual(self.log.getvalue(),  'PASSED: testlog.assertEqual(4, 4)')
