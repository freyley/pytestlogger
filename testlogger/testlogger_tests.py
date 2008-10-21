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
        self.assertEqual(self.log.getvalue(), 'WHAT?')
        
        
