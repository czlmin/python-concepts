import numpy as np

# Read input
N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])

# Print mean along axis 1
print(np.mean(arr, axis=1))

# Print variance along axis 0
print(np.var(arr, axis=0))

# Print standard deviation (rounded to 11 decimal places as HackerRank expects)
print(np.round(np.std(arr), 11))
