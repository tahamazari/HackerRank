#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = []
    right = []

    for i in range(0, len(arr)):
        if(arr[i] < pivot):
            left.append(arr[i])

    for i in range(0, len(arr)):
        if(arr[i] == pivot):
            equal.append(arr[i])

    for i in range(0, len(arr)):
        if(arr[i] > pivot):
            right.append(arr[i])

    arr = left + equal + right
    x = print(*arr)
    x = str(x)
    return arr


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())
    arr = []

    for i in range(0, n):
        item = int(input())
        arr.append(item)

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
