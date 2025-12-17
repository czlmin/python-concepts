# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy


array = list(map(int, input().split()))
my_array = numpy.array(array)
print(numpy.reshape(my_array, (3,3)))