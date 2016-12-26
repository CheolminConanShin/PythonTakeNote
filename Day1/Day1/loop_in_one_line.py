l = list(range(1,10))
# 1 ~ 9

[i**2 for i in l]
# [1, 4, 9, 16...]

d = {100: "apple", 200: "orange", 300: "banana"}
[value.upper() for value in d.values()]
# upper case apple, orange, banana printed