# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations

s, n = input().split()
result = permutations(s, int(n))
sorted_result = sorted(result)
for p in sorted_result:
    s = ''.join(list(p))
    print(s)