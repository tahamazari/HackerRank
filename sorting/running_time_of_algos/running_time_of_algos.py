#!/bin/python3

import math
import os
import random
import re
import sys

def insertion_sort(l):
    shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           l[j+1] = key
           shifts +=1

    print(shifts)
    # print(*l)
    return(shifts)

# Complete the runningTime function below.
def runningTime(arr):
    shifts = insertion_sort(arr)
    return shifts

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    arr = []

    for i in range(0, n):
        item = int(input())
        arr.append(item)

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
