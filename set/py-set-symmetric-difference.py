# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b)))