#coding:utf-8
'''
Created on 2013. 12. 2.

@author: Administrator
'''
class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass
p, s = Person(), Student()
#상속관계를 파악한다. 
print("p is instance of Person: ", isinstance(p, Person))
#버전 3 이후로 모든 클래스는 object에서 파생됨 
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))