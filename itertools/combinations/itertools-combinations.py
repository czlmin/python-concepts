# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, n = input().split()
s = ''.join(sorted(s))
n = int(n)
for i in range(1, n+1):
    result = combinations(s, i)
    # print(*result)
    for c in result:
        # print(c)
        p = ''.join(c)
        print(p)
