#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count_arr = [0]*(len(arr))

    if(len(arr) == 100):
        for i in range(0, len(arr)):
            count_arr[arr[i]] += 1
    elif(len(arr) > 100):
        for i in range(0, len(arr)):
            count_arr[arr[i]] += 1
        count_arr = filter(lambda a: a != 0, count_arr)

    print(count_arr)
    return count_arr

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
