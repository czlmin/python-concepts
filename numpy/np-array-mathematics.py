# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy

N, M = map(int, input().strip().split())
array_a = []
array_b = []
for _ in range(N):
    array_a.append(list(map(int, input().strip().split())))
for _ in range(N):
    array_b.append(list(map(int, input().strip().split())))
my_array_a = numpy.array(array_a, int)
my_array_a.reshape((N, M))
my_array_b = numpy.array(array_b, int)
my_array_b.reshape((N, M))

print(my_array_a + my_array_b)
print(my_array_a - my_array_b)
print(my_array_a * my_array_b)
print(my_array_a // my_array_b)
print(my_array_a % my_array_b)
print(my_array_a ** my_array_b)
