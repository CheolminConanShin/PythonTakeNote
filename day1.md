##강사 소개
- papasmf1@gmail.com
- papasmf.blogspot.kr

### Python 적당한 사용처
- 파이썬은 멀티플래폼 지원
- Server/DB개발에 적합
- ML/AI

### Python 환경 구축
- 데이터 분석시 아나콘다 패키지를 통해 iPython 설치
- [Python 다운로드](https://www.python.org/downloads/)

```python
def intersect(prelist, postlist):
    retList=[]
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

print(intersect('HAM', 'SPAM'))

def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if not x in res:
                res.append(x)
    return res

print(union([1,2,3],[3,4,5],[5,6,7]))

def userURIBuilder(server, port, **user):
    str = "I Love You" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

for item in 'abc':
    print(item)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
# yield를 사용해야 정상적인 iteration이 가능

for char in reverse('gold'):
    print(char)
# return d l o g
```