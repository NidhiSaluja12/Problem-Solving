

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    length = len(arr)
    left = 0
    right= 0
    for i in range(n):
        left+=arr[i][i]
        right+=arr[i][n-i-1]
        res = left-right
    return abs(res)
    
    
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

