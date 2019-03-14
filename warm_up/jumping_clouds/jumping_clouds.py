#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds):
    jumps = 0
    i = 0
    length = 0
    length = len(clouds) - 1

    while i < length:
        if(i < length and clouds[i] == clouds[i+1]):
            i += 1
            if(i < length and clouds[i] == clouds[i+1]):
                jumps += 1
        else:
            i += 1
            jumps += 1

    print(jumps)
    return jumps

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    clouds = []

    for i in range(0, n):
        input_clouds = int(input())
        clouds.append(input_clouds)

    result = jumpingOnClouds(clouds)
    fptr.write(str(result) + '\n')

    fptr.close()
