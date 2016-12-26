def RaiseErrorFunc():
    raise NameError

try:
    RaiseErrorFunc()
except:
    print("NameErrir is Catched")

    
