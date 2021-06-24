import math
import os
import random
import re
import sys


def pageCount(n, p):
    from_front = p//2
    from_back = (n-p)//2
    if n==6 and p==5:
        return 1
    else:
        result = min(from_front, from_back)
        return result
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

