# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    s = input()
    freq = collections.Counter(s)

    top3 = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:3]
    for ch, cnt in top3:
        print(ch, cnt)
