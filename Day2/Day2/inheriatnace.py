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