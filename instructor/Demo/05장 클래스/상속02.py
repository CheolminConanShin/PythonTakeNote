class Person:
    " Super Class "
    def __init__(self, name, phoneNumber):
        self.Name = name 
        self.PhoneNumber = phoneNumber
        
    def PrintInfo(self):
        print("Info(Name:{0}, Phone Number: {1}".format(self.Name, 
                        self.PhoneNumber))
        
    def PrintPersonData(self):
        print("Person(Name:{0}, Phone Number: {1}".format(self.Name, self.PhoneNumber))
       
class Student(Person):
    " Sub Class "
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 Person 생성자를 호출
        Person.__init__(self, name, phoneNumber)
        self.Subject = subject
        self.StudentID = studentID

    def PrintStudentData(self):
        print("Student(Subject: {0}, Student ID: {1}".format(self.Subject,
                                                             self.StudentID))
        
p = Person("Derick", "010-222-3333")
s = Student("Marry", "010-333-4444", "Computer Scient", "990000")

