# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true

import numpy

N = int(input())

my_array1 = numpy.array([list(map(int, input().split())) for _ in range(N)])
my_array2 = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.dot(my_array1, my_array2))
