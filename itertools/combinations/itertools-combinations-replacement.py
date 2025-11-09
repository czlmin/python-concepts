# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement

s, n = input().split()

n = int(n)
s = ''.join(sorted(s))
result = combinations_with_replacement(s, n)
for c in result:
    p = ''.join(c)
    print(p)

