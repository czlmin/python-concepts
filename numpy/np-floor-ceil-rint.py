# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy='1.13')

array = list(map(float, input().strip().split()))
my_array = numpy.array(array)

print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))