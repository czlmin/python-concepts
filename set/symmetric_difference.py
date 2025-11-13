# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

m = int(input())
a = list(map(int, input().split()))
a = set(a)
n = int(input())
b = list(map(int, input().split()))
b = set(b)

diff_a = a.difference(b)
diff_b = b.difference(a)

c = sorted(diff_a.union(diff_b))
for item in c:
    print(item)