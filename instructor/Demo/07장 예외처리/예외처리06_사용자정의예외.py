class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value


def PositiveDivide(a, b):
    if(b < 0):  #0보다 적은 경우 NegativeDivisionError 발생
        raise NegativeDivisionError(b)
    return a / b

try:
    ret = PositiveDivide(10, -3)
    print('10 / 3 = {0}'.format(ret))
except NegativeDivisionError as e:
    print('Error - Second argument of PositiveDivide is ', e.value)
except ZeroDivisionError as e:
    print('Error - ', e.args[0])

    
