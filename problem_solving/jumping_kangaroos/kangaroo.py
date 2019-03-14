#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    print(x1, v1, x2, v2)

    k1 = x1
    k2 = x2

    k1_list = []
    k2_list = []

    answer = ""

    for i in range(0, 10):
        k1_list.append(k1)
        k1 += v1

    for i in range(0, 10):
        k2_list.append(k2)
        k2 +=v2

    for i in range(0, 10):
        if(k1_list[i] == k2_list[i]):
            answer = "YES"
            break
        else:
            answer = "NO"

    print(k1_list)
    print(k2_list)
    print(answer)
    return answer

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    x1 = int(input())

    v1 = int(input())

    x2 = int(input())

    v2 = int(input())

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
