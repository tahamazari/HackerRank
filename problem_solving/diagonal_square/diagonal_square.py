#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    length = 0
    secondary_length = 0

    length = len(arr)
    secondary_length = len(arr) - 1

    primary_sum = 0
    secondary_sum = 0
    x = 0

    for i in range(0, length):
        primary_sum += arr[x][x]
        x += 1

    a = length - 1
    b = 0

    for i in range(0, length):
        secondary_sum += arr[a][b]
        a -= 1
        b += 1

    difference = abs(primary_sum - secondary_sum)

    return difference 

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    arr = []

    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp.append(int(input()))
        arr.append(temp)

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
