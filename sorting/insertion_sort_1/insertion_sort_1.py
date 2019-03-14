#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    end = arr[(len(arr)-1)]

    i = 0
    i = len(arr) - 1

    while i > 0:
        if(end <= arr[i]):
            arr[i] = arr[i-1]
            if(end >= arr[i]):
                arr[i] = end
            if(end < arr[i]):
                arr[i-1] = end
        else:
            break
        print(*arr, "end =>", end)
        i -= 1

if __name__ == '__main__':
    n = int(input())
    arr = []

    for i in range(0, n):
        item = int(input())
        arr.append(item)

    insertionSort1(n, arr)
