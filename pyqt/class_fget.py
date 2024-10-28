class myclass(object):
    def __init__(self):
        self._param=None
    def getparam(self):
        print("get param: %s"%self._param)
        return self._param
    def setparam(self,value):
        print("set value")
        self._param=value
    def delparam(self):
        print("del param")
        del self._param
    param=property(getparam,setparam,delparam)

c1=myclass()
c1.param=10
print("current param:%s"%c1.param)
del c1.param



