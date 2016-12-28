### Day3
##### Exception Handler
```python
# Exception Class Declaration
class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value

def PositiveDivide(a,b):
    if(b < 0):
        raise NegativeDivisionError(b)
    return a / b

try:
    ret = PositiveDivide(10, -3)
    print('10 / -1 = {0}'.format(ret))
except NegativeDivisionError as e:
    print('음수로 나눗셈을 합니다', e.value)
except TypeError as e:
    print('모든 인자는 숫자여야 합니다', e.args[0])
except:
    print('나머지 다른 에러입니다')
finally:
    print('항상 실행되는 블럭입니다')
```
