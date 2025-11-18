# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

n = int(input())
s = list(map(int, input().split()))

counter_s = Counter(s)
for item in counter_s:
    if counter_s[item] != n:
        print(item)
