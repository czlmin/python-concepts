# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

A = set(map(int, input().split()))
N = int(input())
result = 'True'
for i in range(N):
    s = set(map(int, input().split()))
    if not A.issuperset(s):
        result = 'False'
print(result)