import unittest
import exceptions
import inspect
import sys
import datetime
import traceback

def wrap_method(method,  methodname):
    # retrieve the enclosing class of the method
    class_ = method.im_class

    def alias_method(self,  *args, **kwargs):
        retval = None
        try:
            retval = method(self, *args, **kwargs)
            if self.logSuccesses:
                codeline = self._reportLine(inspect.stack())
                self.logger('PASSED: ' + codeline,  False)
        except exceptions.AssertionError,  ae:
            codeline = self._reportLine(inspect.stack())
            self.logger('FAILED: ' + ae.message + ' in ' + codeline)
        return retval
    # replace the original method with the alias
    setattr(class_, methodname, alias_method)


class TestLogger(unittest.TestCase):
    '''See unittest.TestCase documentation for how assert and fail methods operate'''
    def __init__(self):
        self.reset()
        super(TestLogger,  self).__init__()

    def runTest(self):
        '''This TestCase logs errors in running code'''
        pass

    #def logger(self,  report):
    #    '''The default logger.'''
    #    print "No logger defined. This shouldn't happen."

    def reset(self):
        '''Reset this TestLogger to the defaults'''
        self.logSuccesses = False
        self.verbose = False
        def stderrlogger(report,  fail=True):
            '''stderr logger sends messages to stderr'''
            sys.stderr.writelines(str(datetime.datetime.now())+': '+report)
        self.logger = stderrlogger
        
    def log_to_file(self, fp):
        '''Instruct this testlogger to log to a file.
           Takes an open, writeable file object
           Or a string with a file location.'''
        if type(fp) == type(''):
            fp = open(fp, 'w')
        a = '''filelogger sends messages to file %s''' % fp.name
        def filelogger(report,  fail = True):
            a
            fp.write(str(datetime.datetime.now())+': '+report + u'\n')
        self.logger = filelogger

    def log_to_logging(self,  logging):
        '''Instruct this testlogger to log to a logging object.
           Takes a logging object.'''
        def logginglogger(report,  fail=True):
            '''logginglogger sends messages to a logging object'''
            if fail:
                logging.error(report)
            else:
                logging.info(report)
        self.logger = logginglogger

    def set_verbose(self, verbose):
        '''Instruct this testlogger to print stacktraces or not.
           Default is not verbose.
           Takes True or False'''
        self.assert_(verbose in [False, True], 'testlog.set_verbose takes True or False, not %s.' %str(verbose))
        self.verbose = verbose

    def _reportLine(self,  stack):
        '''Internal. Do not use.'''
        if stack[1][4]:
            if self.verbose:
                codeline = stack[1][1] + ' line ' + str(stack[1][2]) + ': ' + stack[1][4][0].strip()
                codeline += '\nStacktrace\n'
                codeline += ''.join(traceback.format_stack()[:-2])
                codeline += '\n'
            else:
                codeline = stack[1][1] + ' line ' + str(stack[1][2]) + ': ' + stack[1][4][0].strip()
        else:
            codeline = ' console'
        return codeline

filterfunc = lambda x: ((x.startswith('assert') or x.startswith('fail')) and not x.endswith('Exception'))
functions = filter(filterfunc,  dir(TestLogger))
for funcname in functions:
    func = getattr(TestLogger,  funcname)
    wrap_method(func,  funcname)
