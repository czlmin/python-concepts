# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy

N, M = map(int, input().strip().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

my_array = numpy.array(array)
my_array = numpy.min(my_array, axis=1)
print(numpy.max(my_array))