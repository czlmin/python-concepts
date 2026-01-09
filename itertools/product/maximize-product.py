# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

n, M = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(n)] # in the question, the first number is the metadata (the number of elements)

# All combinations, one element from each list
max_value = 0
final_combo = None
for combo in product(*lists):
    total = sum(x**2 for x in combo) % M
    if total > max_value:
        max_value = total
        final_combo = combo

print(max_value)
print(final_combo)
