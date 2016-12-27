class CounterManager:
    __insCount = 0
    def __init__(self):
        CounterManager.__insCount += 1
    @staticmethod #데코레이터 선언(어노테이션)
    def staticPrintCount():  #정적 메서드 정의 
        print("Instance Count: ", CounterManager.__insCount)
    @classmethod
    def classPrintCount(cls): #클래스 메서드 정의(암묵적으로 첫 인자는 클래스를 받음)
        print("Instance Count: ", cls.__insCount)
        
a, b, c = CounterManager(), CounterManager(), CounterManager()

#정적 메서드로 인스턴스 객체 개수를 출력 
CounterManager.staticPrintCount()
b.SPrintCount()
#클래스 메서드로 인스턴스 객체 개수를 출력 
CounterManager.classPrintCount()
