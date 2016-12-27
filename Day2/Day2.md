### Day 2

##### Filtering
###### Without Filter
```python
>>> L = [10,25,30]
>>> IterL = filter(None, L)
>>> for item in IterL:
	print(item)
10
25
30
```
###### With Filter
```python
>>> def GetBiggerThan20(i):
	return i > 20
>>> IterL = filter(GetBiggerThan20, L)
>>> for item in IterL:
	print(item)
25
30
```
###### With Filter and Lambda
```python
>>> IterL = filter(lambda i:i>20, L)
>>> for item in IterL:
	print(item)
25
30
```

##### Zip
```python
>>> x = [10, 20, 30]
>>> y = ['A', 'B', 'C']
>>> retList = list(zip(x,y))
>>> retList
[(10, 'A'), (20, 'B'), (30, 'C')]
```

##### Map
```python
>>> L = [1, 2, 3]
>>> def Add10(i):
	return i + 10
>>> for i in map(Add10, L):
	print(i)
11
12
13
```
