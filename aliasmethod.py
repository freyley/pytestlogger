import inspect

class A(object):
    def a(self,  a,  b):
        pass
    
    def b(self,  b):
        pass
    
    def c(self,  foo = None):
        pass

class B(A):
    def __init__(self):
        for func in filter(lambda x: len(x) == 1,  dir(self)):
            func = getattr(self,  func)
            def method(*args,  **kwargs):
                print 'beginning'
                retval = func(*args,  **kwargs)
                print 'ending'
                return retval
            setattr(self,  func.__name__,  method)
