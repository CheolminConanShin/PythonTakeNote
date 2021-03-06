### Day 2

##### Filtering
###### Without Filter
```python
>>> L = [10,25,30]
>>> IterL = filter(None, L)
>>> for item in IterL:
	print(item)
10
25
30
```
###### With Filter
```python
>>> def GetBiggerThan20(i):
	return i > 20
>>> IterL = filter(GetBiggerThan20, L)
>>> for item in IterL:
	print(item)
25
30
```
###### With Filter and Lambda
```python
>>> IterL = filter(lambda i:i>20, L)
>>> for item in IterL:
	print(item)
25
30
```

##### Zip
```python
>>> x = [10, 20, 30]
>>> y = ['A', 'B', 'C']
>>> retList = list(zip(x,y))
>>> retList
[(10, 'A'), (20, 'B'), (30, 'C')]
```

##### Map
```python
>>> L = [1, 2, 3]
>>> def Add10(i):
	return i + 10
>>> for i in map(Add10, L):
	print(i)
11
12
13
```

##### Python Class Declaration
```python
>>> class Person:
	"""클래스에 대한 설명을 다중 라인으로
	추가할 경우에 사용"""

	Name = "Default Name"
	def Print(self):
		print("My name is {0}".format(self.Name))
>>> p1 = Person()
>>> p1.Print()
My name is Default Name
```

##### Python Runtime Characteristic
```python
	# Python은 런타임에서 클래스나 인스턴스에 속성을 추가/수정 할 수 있다.
>>> p1 = Person()
>>> p1.NewName = "New Conan"
>>> p1.Name = "Conan"
```

##### Inheritance
```python
class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass
p, s = Person(), Student()
print("p is instance of Person", isinstance(p, Person))
print("s is instance of Student", isinstance(s, Student))
print("s is instance of Person", isinstance(s, Person))
print("p is instance of Bird", isinstance(p, Bird))
print("p is instance of object", isinstance(p, object))
p is instance of Person True
s is instance of Student True
s is instance of Person True
p is instance of Bird False
p is instance of object True
```

##### Multiple Inheritance
```python
class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Cry(self):
        print("호랑이 어흥")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")
    def Cry(self):
        print("사자 으르릉")

class Liger(Tiger, Lion):
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")

l = Liger()
l.Jump() #호랑이처럼 멀리 점프하기 출력
l.Play() #라이거만의 사육사와 재미있게 놀기 출력
l.Cry() #호랑이 어흥 출력
print("mro순서: ", Liger.__mro__)
#mro순서:  (<class '__main__.Liger'>, <class '__main__.Tiger'>, <class '__main__.Lion'>, <class 'object'>)
```

##### Subclass
```python
class Person:
    "부모 클래스"
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    def PrintInfo(self):
        print("Info name:{0}, phoneNumber:{1}".format(self.Name, self.PhoneNumber))
    def PrintPersonData(self):
        print("Person Info name:{0}, phoneNumber:{1}".format(self.Name, self.PhoneNumber))

class Student(Person):
    "자식 클래스"
    def __init__(self, name, phoneNumber, subject, studentID):
        #Super Class Constructor Call
        Person.__init__(self, name, phoneNumber)
        self.Subject = subject
        self.StudentID = studentID
    def PrintInfo(self):
        #Method Override
        print("Info name:{0}, phoneNumber:{1}".format(self.Name, self.PhoneNumber))
        print("Info subject:{0}, studentID:{1}".format(self.Subject, self.StudentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-123-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)
print("Student is subclass of Person", issubclass(Student, Person)) #True
print("Person is subclass of Student", issubclass(Person, Student)) #False
p.PrintInfo() #이름 전화번호 출력
s.PrintInfo() #이름 전화번호 전공 학번 출력
```

##### Class Constructor/Destructor
```python
class MyClass:
    def __init__(self, value):
        print("Class is created!")
        selfValue = value
    def __del__(self):
        print("Class is deleted!")

d = MyClass(10)
d_copy = d
del d
del d_copy
Class is created!
Class is deleted!
```

##### Primitive Operators Override
```python
class NumBox:
    def __init__(self, num):
        self.Num = num
    def __add__(self, num):
        self.Num += num
    def __sub__(self, num):
        self.Num -= num

n = NumBox(40)
n + 100
print(n.Num)
140
```

##### Module Reload without Restart from Console
```python
import imp
imp.reload(module_name)
```

##### Private Member Variable
```python
class CounterManager:
    __insCount = 0 #Private Member Variable은 _를 두개 앞에다가 붙인다.
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
b.staticPrintCount()
#클래스 메서드로 인스턴스 객체 개수를 출력 
CounterManager.classPrintCount()
print("내부변수값: ", CounterManager._CounterManager__insCount)
```