# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

s = input().strip()

# Pattern:
# (?<=[^aeiouAEIOU])   → preceded by a non-vowel
# ([aeiouAEIOU]{2,})   → capture 2+ vowels
# (?=[^aeiouAEIOU])    → followed by a non-vowel
pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

matches = re.findall(pattern, s)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)
