0#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max = 0
    count = 0
    a = 0
    b = 0

    for i in range(0, len(ar) - 1):
        if(max <= ar[a+1]):
            max = ar[a+1]
        a +=1

    for i in range(0, len(ar)):
        if(ar[b] == max):
            count += 1
        b += 1

    print(max, "is max")
    print(count, "is count")
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    ar = []

    for i in range(0, n):
        item = int(input())
        ar.append(item)

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
