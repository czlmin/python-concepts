# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re

regex_pattern = r"([a-zA-Z0-9])\1+"
pattern = re.search(regex_pattern, input())
if pattern:
    print(pattern.group()[0])
else:
    print("-1")
