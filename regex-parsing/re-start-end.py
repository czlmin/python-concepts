# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

s = input().strip()
k = input().strip()

# Build a lookahead pattern so we can find overlapping matches
pattern = re.compile(r'(?={})'.format(re.escape(k)))

matches = list(pattern.finditer(s))

if not matches:
    print((-1, -1))
else:
    for m in matches:
        start = m.start()
        end = start + len(k) - 1
        print((start, end))
