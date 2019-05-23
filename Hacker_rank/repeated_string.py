#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    x = 0
    # for i in s:
    #     s += str(i)
    #     x += 1
    #     if( x < n):
    #         for j in s:
    #             s += str(j)
    #
    # total_a = 0
    #
    # a = 0
    # while a < n:
    #     if(s[a] == 'a'):
    #         total_a += 1
    #     a += 1

    # for a in range(0, n):
    #     if(a < n and s[a] == 'a'):
    #         total_a += 1
    total_a = 0
    x = 0

    for i in s:
        if(i == 'a'):
            total_a += 1

    print(total_a)
    return total_a

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
