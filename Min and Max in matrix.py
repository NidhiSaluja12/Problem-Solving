import numpy
M,N = map(int, input().split())
arr = numpy.array([input().split() for i in range(N)], int)
minimum = numpy.min(arr, axis=1)
maximum = numpy.max(minimum)
print(maximum)


