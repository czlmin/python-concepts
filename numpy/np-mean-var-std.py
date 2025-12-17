# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy

N, M = map(int, input().split())
my_array = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(numpy.round(numpy.std(my_array), 11))