import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    arrival_on_time = 0
    arrival_late = 0
    for i in range (len(a)):
        if a[i] <= 0:
            arrival_on_time += 1
        elif a[i] > 0:
            arrival_late += 1
    if arrival_on_time < k:
        return "YES"
    else:
        return "NO"
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')
    fptr.close()

