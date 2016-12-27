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

##### Python Inheritance
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

##### Class De/Constructor
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
