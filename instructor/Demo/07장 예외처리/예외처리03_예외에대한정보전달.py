def divide(a, b):
    return a / b

try:
    c = divide(5, 'string')
except TypeError as e:
    print('에러: ', e.args[0])
except Exception:
    print('무슨 에러인지 모르겠습니다')
    
