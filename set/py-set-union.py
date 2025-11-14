# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.union(b)))