from TestLogger import TestLogger


def report_line(stack):
    codeline = stack[2][1] + ' line ' + str(stack[2][2]) + ': ' + stack[2][4][0].strip()
    return codeline

def replace_method(method):
    class_ = method.im_class
    name_ = method.__name__
    def alias_method(self, *args,  **kwargs):
        retval = None
        try:
            retval = method(*args,  **kwargs)
            if self.logSuccesses:
                codeline = self.reportLine(inspect.stack())
                self.logger('PASSED: ' + codeline)
        except exceptions.AssertionError,  ae:
            codeline = self.reportLine(inspect.stack())
            self.logger('FAILED: ' + ae.message + ' in ' + codeline)
        finally:
            return retval
    setattr(class_,  name_,  alias_method)

def wrap_asserts(obj):
    funcs = dir(obj)
    filterfunction = lambda x: (x.startswith('assert') or x.startswith('fail')) and not x.endswith('Exception')
    funcs = filter(filterfunction,  funcs)
    for func in funcs:
        func = getattr(obj,  func)
        replace_method(func)


#testlog = TestLogger()
#testlog.reset()
#wrap_asserts(testlog)


    
    
