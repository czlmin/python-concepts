# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy

N, M = map(int, input().strip().split())

array = []
for i in range(N):
    array.append(list(map(int, input().strip().split())))

my_array = numpy.array(array)
my_array = numpy.reshape(my_array, (N, M))
print(my_array.transpose())
print(my_array.flatten())