# Try Exception
def divide(a,b):
    return a / b

try:
    c = divide(5, 2)
except (ZeroDivisionError, OverflowError, FloatingPointError):
    print('두번째 인자가 0이면 안됩니다')
except TypeError as e:
    print('모든 인자는 숫자여야 합니다', e.args[0])
except:
    print('나머지 다른 에러입니다')
else:
    print("결과:{0}".format(c))
finally:
    print("항상 실행되는 블럭")
