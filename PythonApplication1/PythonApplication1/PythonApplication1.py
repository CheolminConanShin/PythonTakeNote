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