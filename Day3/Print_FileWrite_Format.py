import sys
print("Welcome to", "Python", sep='-', end='!', file=sys.stderr)
# Welcome to-Python!

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

# 오른쪽 정렬 3자리
for x in range(1,6):
    print(x, '*', x, '=', str(x*x).rjust(3))

# Padding
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