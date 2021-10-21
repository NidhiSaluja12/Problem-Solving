import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    catA = abs(z-x)
    catB = abs(z-y)
    if catA>catB:
        return "Cat B"
    elif catB>catA:
        return "Cat A"
    elif catA==catB:
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

