# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy

N, M = map(int, input().strip().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

my_array = numpy.array(array)
my_array = numpy.sum(my_array, axis=0)
print(numpy.prod(my_array))