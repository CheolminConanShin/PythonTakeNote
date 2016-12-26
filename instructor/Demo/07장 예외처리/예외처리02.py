def divide(a, b):
    return a / b

try:
    c = divide(5, 'string')
except ZeroDivisionError:
    print('두 번째 인자는 0이여서는 안됩니다.')
except TypeError:
    print('모든 인자는 숫자여야 합니다.')
except:
    print('ZeroDivisionError, TypeError를 제외한 다른 에러')
else:
    print('Result: {0}'.format(c))
finally:
    print('항상 finally 블럭은 수행됩니다')
    
    
