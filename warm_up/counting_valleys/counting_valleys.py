import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    level = 0
    count = 0

    for i in range(0, n):
        if(s[i] == "u"):
            level = level + 1
            if(level == 0):
                valleys += 1
        elif(s[i] == "d"):
            level = level - 1

    print(valleys)
    return valleys

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())
    s = []
    for i in range(0, n):
        input_string = str(input())
        s.append(input_string)

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
