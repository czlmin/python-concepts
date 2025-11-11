# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

n, p = map(int, input().split())
lists = []
data = []
for i in range(n):
    data = list(map(int, input().split()))
    lists.append(data[1:])
dsum = 0
for i in range(n):
    dmax = max(lists[i])
    dsum += dmax ** 2

x = dsum % p
print(x)

