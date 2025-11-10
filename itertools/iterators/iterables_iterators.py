from itertools import combinations

def iterables_iterators(s, k):
    n = len(s)
    s_na = [im for im in s if im != 'a']
    n_na = len(s_na)

    if 'a' not in s:
        p = 0.0
    elif k > n:
        p = 0.0
    elif n_na < k:
        p = 1.0
    else:
        p = 1 - len(list(combinations(s_na, k))) / len(list(combinations(s, k)))

    return round(p, 4)

input()
s = input().split()
k = int(input())
s = "".join(s)
print(iterables_iterators(s, k))
