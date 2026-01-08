# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# def solve(s):
#     names = s.split(' ')
#     cap_names = []
#     for name in names:
#         if len(name) > 1:
#             new_name = name[0].upper() + name[1:]
#         else:
#             new_name = name.upper()
#         cap_names.append(new_name)
#     return ' '.join(cap_names)

def solve(s):
    return ' '.join(w.capitalize() for w in s.split(' '))

if __name__ == '__main__':
    s = input()
    print(solve(s))