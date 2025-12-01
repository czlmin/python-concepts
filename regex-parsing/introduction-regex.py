# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re

pattern = re.compile(r'^[+-]?\d*\.\d+$')

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(bool(pattern.match(s)))
