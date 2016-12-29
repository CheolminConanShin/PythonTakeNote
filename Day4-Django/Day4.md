### Day 4
##### Time
```python
>>> import time
>>> time.time()
1482972896.302908
>>> time.gmtime()
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=29, tm_hour=0, tm_min=55, tm_sec=47, tm_wday=3, tm_yday=364, tm_isdst=0)
>>> time.localtime()
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=29, tm_hour=9, tm_min=55, tm_sec=52, tm_wday=3, tm_yday=364, tm_isdst=0)
>>> import datetime
>>> datetime.date(2016, 12, 10)
datetime.date(2016, 12, 10)
>>> d = datetime.date(2016, 12, 10)
>>> d.month
12
>>> datetime.date.today()
datetime.date(2016, 12, 29)
>>> d2 = datetime.date.today()
>>> d2.min
datetime.date(1, 1, 1)
>>> d2.max
datetime.date(9999, 12, 31)
```

##### Time Difference
```python
td_1 = timedelta(hours=7)
>>> td_2 = timedelta(days=3)
>>> td_1 + td_2
datetime.timedelta(3, 25200)
>>> td_2 = timedelta(days=-3)
>>> td_1 + td_2
datetime.timedelta(-3, 25200)
```

##### Math
```python
import math
>>> lst = list(range(1, 101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
>>> sum(lst)
5050
>>> max(lst)
100
>>> min(lst)
1
>>> math.factorial(10)
3628800
>>> math.ceil(3.14)
4
>>> math.floor(3.14)
3
```

##### Random
```python
import random
>>> random.random()
0.7951378185676322
>>> random.uniform(3, 4)
3.0412322285155717
>>> [random.randrange(20) for i in range(10)]
[10, 17, 11, 18, 5, 14, 3, 4, 15, 12] # 중복이 있을 수 있음
>>> random.sample(range(20), 10)
[13, 4, 12, 18, 10, 2, 7, 16, 9, 15] # 중복이 없음
>>> lotto =list(range(1,46))
>>> random.shuffle(lotto) # 순서를 섞음
>>> lotto
[15, 10, 39, 41, 34, 1, 19, ...]
```

##### Path
```python
from os.path import *
>>> abspath('tmp')
'C:\\Python34\\tmp'
>>> basename('c:\\python34\\python.exe')
'python.exe'
>>> exists('c:\\python34\\python.exe')
True
>>> getsize('c:\\python34\\python.exe')
27136
>>> isfile('c:\\python34\\python.exe')
True
```
##### OS Library
```python
from os import *
>>> getcwd()
'C:\\Python34'
>>> chdir('..')
>>> getcwd()
'C:\\'
>>> name
'nt' # OS Name
>>> environ # 환경 변수를 출력
>>> list(environ.keys()) # 환경 변수 Key값만 출력
>>> system('calc') # 계산기를 실행하는 시스템 함수
```

##### Glob Library
```python
import glob
for item in glob.glob('*.*'):
	print(item)
# 현재 위치에서 모든 파일을 출력
```