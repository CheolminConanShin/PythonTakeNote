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