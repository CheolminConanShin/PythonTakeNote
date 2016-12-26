class CounterManager:
    __insCount = 0
    def __init__(self):
        CounterManager.__insCount += 1
    def staticPrintCount():
        print("Instance Count: %d" % CounterManager.__insCount)
    SPrintCount = staticmethod(staticPrintCount)  #정적 메서드로 등록

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.SPrintCount() 
    
print(CounterManager.__insCount)
