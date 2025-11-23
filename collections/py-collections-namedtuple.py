# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple

N = int(input())
names = input().split()
Student = namedtuple("Student", names)

total_marks = 0
for _ in range(N):
    row = input().split()
    student = Student(*row)
    total_marks += int(student.MARKS)

average = total_marks / N
print(f'{average:.2f}')
