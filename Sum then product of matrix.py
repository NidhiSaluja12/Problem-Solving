import numpy
M,N = map(int, input().split())
arr = numpy.array([input().split() for i in range(N)] , int)
summ = numpy.sum(arr, axis = 0)
product = numpy.prod(summ)
print(product)

