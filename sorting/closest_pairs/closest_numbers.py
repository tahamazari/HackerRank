#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def print_tuples(ts):
    for a, b in ts:
        print(a, b)


def closest_numbers(a):
    a = sorted(a)
    pairs = []
    current_min = sys.maxsize
    for idx in range(1, len(a)):
        diff = a[idx] - a[idx - 1]
        if (a[idx] - a[idx - 1] == current_min):
            pairs.append((a[idx - 1], a[idx]))
        elif (diff < current_min):
            pairs = []
            current_min = a[idx] - a[idx - 1]
            pairs.append((a[idx - 1], a[idx]))
    return pairs

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closest_numbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
