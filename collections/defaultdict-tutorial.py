#

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().strip().split())
for i in range(n):
    word = input().strip()
    d[word].append(i+1)
for j in range(m):
    word_b = input().strip()
    if word_b not in d.keys():
        list_index = [-1]
    else:
        list_index = d[word_b]
    print(' '.join(list(map(str, list_index))))

