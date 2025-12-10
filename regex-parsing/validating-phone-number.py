# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import re

N = int(input().strip())
regex_pattern = r"^[7-9]{1}\d{9}$"
pattern = re.compile(regex_pattern)
for _ in range(N):
    s = input().strip()
    if pattern.match(s):
        print("YES")
    else:
        print("NO")