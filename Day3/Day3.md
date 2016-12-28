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

##### Print
```python
print("Welcome to", "Python", sep='-', end='!', file=sys.stderr)
# Welcome to-Python!
```

##### File Read & Write
```python
# Print로 파일 쓰기
f = open("C:\\Users\\student\\Documents\\note\\Day3\\data.txt", "wt")
print("file write", file=f)
f.close()
f.closed

# 파일 쓰기
f = open("C:\\Users\\student\\Documents\\note\\Day3\\data.txt", "wt")
f.write("한글로 문자열 저장\n")
f.write("1234\n")
f.close()

# 파일 읽기
f = open("C:\\Users\\student\\Documents\\note\\Day3\\data.txt", "rt")
f.read()
f.close()

# 한줄씩 불러오기
f = open("C:\\Users\\student\\Documents\\note\\Day3\\data.txt", "rt")
lst = f.readlines()
for item in lst:
    print(item)
f.close()
```

##### Formatting
```python
# 오른쪽 정렬 3자리
for x in range(1,6):
    print(x, '*', x, '=', str(x*x).rjust(3))

# 주로 사용되는 format
print("{0:$>+5}".format(10)) # $$+10
print("{0:$<+5}".format(10)) # $$+10
print("{0:$>-5}".format(10)) # $$$10
print("{0:$>-5}".format(-10)) # $$-10
print("{0:,}".format(12000)) # 12,000
print("{0:x}".format(10)) # 16진수 a
print("{0:b}".format(10)) # 2진수 1010
print("{0:e}".format(4/3)) # 1.333333e+00
print("{0:f}".format(4/3)) # 1.333333
print("{0:.2f}".format(4/3)) # 자리수 표시 1.33
```

##### Translation Map
```python
transmap = str.maketrans("poieu", "P0129")
"python is powerful".translate(transmap)
# 'Pyth0n 1s P0w2rf9l'
```

##### Match Search Split with Regular Expression
```python
bool(re.match('[0-9]*th','    35th'))
# False
bool(re.search('[0-9]*th','    35th'))
# True
>>> bool(re.search('\\\\\w+','\\apple'))
# True
bool(re.search(r'\\\w+',r'\apple'))
# 백 슬레시가 몇개가 오든 상관없이 True

# *은 0 ~ n개, +는 1 ~ n개, ?는 0이나 1개의 문자를 의미
import re
re.split('[:. ]', "apple orange:banana.tomato")
# ['apple', 'orange', 'banana', 'tomato']
re.split('[:. ]+', 'apple orange:::::banana...tomato')
# ['apple', 'orange', 'banana', 'tomato']
re.split('([:. ])+', 'apple orange::::banana..tomato')
# ['apple', ' ', 'orange', ':', 'banana', '.', 'tomato']
```

##### Substitution
```python
import re
"""sub함수는 문자열에 해당 그룹을 치환해주는 작업을 한다
정규식에서 괄호()는 그룹을 의미하며 1번째 그룹을 치환 시켜준다."""
re.sub(r"\b(\d{4}-\d{4})\b", r"<I>\1</I>", "Copyright Derick 1990-2000")
# 'Copyright Derick <I>1990-2000</I>'
```

##### Find & Findall
Find는 해당 문자가 가장처음 발견되면 리턴
Findall은 해당 문자를 모두 리턴...?
```python
import re
s = "Pen Pineapple Apple Pen"
c = re.compile('Pen')
c.findall(s)
# ['Pen', 'Pen']
c = re.compile('apple', re.I)
c.findall(s)
# ['apple', 'Apple'] re.I는 대소문자 구분 없이 re.M은 다중 행
```

##### Match
```python
import re
telChecker = re.compile(r'(\d{2,3})-(\d{3,4})-(\d{4})')
bool(telChecker.match("010-1111-1111"))
# True
m = telChecker.match("010-111-1111")
m.groups()
# ('010', '111', '1111')
m.group(2)
# '111'
```
