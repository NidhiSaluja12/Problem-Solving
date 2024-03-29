import math
import os
import random
import re
import sys



# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    #For lesser elements
    # pair = 0
    # for i in arr:
    #     for j in range(len(arr)):
    #         if i-arr[j] == k:
    #             pair+=1
    # return pair

    #For more elements
    count = 0
    arr = set(arr)
    count = 0
    for num in arr:
        if(num+k in arr):
            count += 1
    return count
                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

