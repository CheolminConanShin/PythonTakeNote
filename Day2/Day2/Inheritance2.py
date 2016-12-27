#부모 클래스
class SuperClass:
    x = 10
    def PrintX(self):
        print(self.x)

#자식 클래스
class SubClass(SuperClass):
    y = 20
    def PrintY(self):
        print(self.y)
    def PrintX(self):
        print("Subclass: ", self.x)

#인스턴스 생성
s = SubClass()
s.a = 5
print("SuperClass: ", SuperClass.__dict__)
print("SubClass: ", SubClass.__dict__)
print("s: ", s.__dict__) #s는 a값만 가지고 있는걸 확인할 수 있다.
#파이썬은 메모리를 최적화하기 위해 부모클래스를 인스턴스는 레퍼런스만 하고 있다.