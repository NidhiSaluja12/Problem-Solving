import numpy
N,M = map(int, input().split())

arr = numpy.array([input().split() for i in range(N)], int)
mean = numpy.mean(arr, axis=1)
var = numpy.var(arr,axis=0)
std = numpy.std(arr)


print(mean)


print(var)
#numpy.set_printoptions(legacy='1.13')
print(round(std,11))




