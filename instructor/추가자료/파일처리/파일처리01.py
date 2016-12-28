import re
f = open("c:\\work\\data.txt")
result = []
lines = f.readlines()
for item in lines:
    if (re.search('aa*',item)):
        result.append(item)

for item in result:
        print(item)
