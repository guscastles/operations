"""
Tail call functions and classes.
"""


class TailCaller(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ret = self.func(*args, **kwargs)
        while isinstance(ret, TailCall):
            ret = ret.handle()
        return ret
 

class TailCall(object):

    def __init__(self, caller, *args, **kwargs):
        self.caller = caller
        self.args = args
        self.kwargs = kwargs

    def handle(self):
        if isinstance(self.caller, TailCaller):
            return self.caller.func(*self.args, **self.kwargs)
        return self.caller
 
