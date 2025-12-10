# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re

regex_pattern = r"(?<=[:\s,])#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})\b"

N = int(input())
for _ in range(N):
    css = input()
    words = re.findall(regex_pattern, css)
    for word in words:
        print("#" + word)