#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    same_pairs = 0
    i = 0
    ar.sort()
    print(ar)
    while i < (n-1):
        if(i < n and ar[i] == ar[i+1]):
            same_pairs += 1
            i = i + 2
        else:
            i += 1

    print('total pairs = ', same_pairs)
    return same_pairs

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']

    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())
    ar = []
    for i in range(0, n):
        number = int(input())
        ar.append(number)

    result = ar

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
