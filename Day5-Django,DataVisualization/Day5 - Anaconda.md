### Anaconda
#### Installation
- [Anaconda Download](https://docs.continuum.io/anaconda/install)
- 설치시 'just me' 선택
- Jupyter QtConsole에서 `%pylab` 실행

#### Read CSV Data File
```python
import pandas as pd
df = pd.read_csv('csv_file_path.csv')
"""
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
"""
# 해더 없이 출력
!type csv_file_path.csv 
"""
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
"""
# 해더 셋팅 출력
df2 = pd.read_csv('file_path.csv', names = ['a', 'b', 'c', 'd', 'message'])
"""
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
"""
!type file_path.csv
"""
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
"""
# 필요 없는 행 Skip
pd.read_csv('file_path.csv', skiprows = [0, 2, 3])
"""
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
"""
```

#### Merge Two CSV files
```python
# Union All
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1':range(7)})
"""
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   a
6      6   b
"""
df2 = DataFrame({'key':['a', 'b', 'd'], 'data2': range(3)})
"""
   data2 key
0      0   a
1      1   b
2      2   d
"""
pd.merge(df1, df2, on='key')
"""
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0
"""
# 교집합
df3 = DataFrame({'lkey':['b', 'b', 'a','c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey':['a', 'b', 'd'], 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')
"""
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a
"""
# Concatenate
s1 = Series([0, 1], index = ['a', 'b'])
"""
a    0
b    1
"""
s2 = Series([2,3,4], index = ['c', 'd', 'e'])
s3 = Series([5,6], index = ['f', 'g'])
pd.concat([s1, s2, s3])
"""
a    0
b    1
c    2
d    3
e    4
f    5
g    6
"""
```
#### Plot Figure
```python
%pylab
fig = plt.figure() # Figure을 생성
# 그래프 3개 생성
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# 마지막 그래프에 Line Chart Plot
from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--')
# 첫번째 그래프에 Bar Chart Plot
ax1.hist(randn(100), bins=20, color='g', alpha=0.9)
# 두번째 그래프에 Scatter Chart Plot
ax2.scatter(np.arange(30), np.arange(30) + 3*randn(30))
```