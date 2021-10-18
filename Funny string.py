import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.





def funnyString(s):
    rev = s[::-1]
    
    for i in range (1, len(s)):
        if (abs(ord(s[i])-ord(s[i-1]))) != (abs(ord(rev[i])-ord(rev[i-1]))):
            return "Not Funny"
        
    return "Funny"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

