# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy

N = int(input())
my_array = numpy.array([list(map(float, input().split())) for _ in range(N)])
print(round(numpy.linalg.det(my_array), 2))