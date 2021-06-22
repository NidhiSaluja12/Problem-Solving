import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    s11 = set(s1)
    s21 = set(s2)
    result = s11.intersection(s21)
    if not result:
        return 'NO'
    else:
        return 'YES'
    
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

