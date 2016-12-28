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