class CounterManager:
    __insCount = 0
    def __init__(self):
        CounterManager.__insCount += 1
    @staticmethod #���ڷ����� ����(������̼�)
    def staticPrintCount():  #���� �޼��� ���� 
        print("Instance Count: ", CounterManager.__insCount)
    @classmethod
    def classPrintCount(cls): #Ŭ���� �޼��� ����(�Ϲ������� ù ���ڴ� Ŭ������ ����)
        print("Instance Count: ", cls.__insCount)
        
a, b, c = CounterManager(), CounterManager(), CounterManager()

#���� �޼���� �ν��Ͻ� ��ü ������ ��� 
CounterManager.staticPrintCount()
b.SPrintCount()
#Ŭ���� �޼���� �ν��Ͻ� ��ü ������ ��� 
CounterManager.classPrintCount()
