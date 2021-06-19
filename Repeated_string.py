import math
import os
import random
import re
import sys


def repeatedString(s, n):
    num = n//len(s)
    rem = n%len(s)
    return num*(s.count('a'))+s[:rem].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

