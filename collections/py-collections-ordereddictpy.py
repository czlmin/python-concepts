# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict

N = int(input())
ordered_dict = OrderedDict()
for _ in range(N):
    item = input().split()
    name = ' '.join(item[:-1])
    price = int(item[-1])
    if name in ordered_dict.keys():
        ordered_dict[name] += price
    else:
        ordered_dict[name] = price
for key, value in ordered_dict.items():
    print(f"{key} {value}")
