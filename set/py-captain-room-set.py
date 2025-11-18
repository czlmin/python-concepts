# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

n = int(input())
s = list(map(int, input().split()))
dup, seen = set(), set()

for item in s:
    if item in seen:
        dup.add(item)
    else:
        seen.add(item)
print(seen.difference(dup).pop())