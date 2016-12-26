#if else example
score = int(input("input score:"))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
else:
    grade = 'D'

print('score: ' + grade)