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
    str = "http://" + server + ":" + port + "/?"
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
# use yield instead of return for iteration

for char in reverse('gold'):
    print(char)
# return d l o g
