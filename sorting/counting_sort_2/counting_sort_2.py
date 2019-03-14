#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    sorted_array = []
    count_array = [0]*(len(arr))

    for i in range(0, len(arr)):
        count_array[arr[i]] += 1

    for i in range(0, len(arr)):
        if(count_array[i] != 0):
            j = 0
            while j < count_array[i]:
                sorted_array.append(i)
                j += 1
    print(sorted_array)

    return sorted_array

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
