class SuperClass:
    x = 10
    def printX(self):
        print(self.x)

class SubClass(SuperClass):
    y = 20
    def printX(self):
        print("SubClass:", self.x)
    def printY(self):
        print(self.y)
    
        
s = SubClass()
s.a = 30
s.x = 50
print("SuperClass: ", SuperClass.__dict__)
print("SubClass: ", SubClass.__dict__)
print("s: ", s.__dict__)
