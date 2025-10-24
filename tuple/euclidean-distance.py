import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

p1 = (1, 2)
p2 = (4, 6)
print(euclidean_distance(p1, p2))