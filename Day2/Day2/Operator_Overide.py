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
n - 50
print(n.Num)