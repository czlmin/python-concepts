# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
from itertools import groupby

s = input()

tpls = []
for key, group in groupby(s):
    # print(key, list(group))
    tpl = (len(list(group)), int(key))
    tpls.append(str(tpl))

print(' '.join(tpls))