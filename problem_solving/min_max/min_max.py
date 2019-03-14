#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_list = []
    min_list = []

    max_sum = 0
    min_sum = 0

    min_num = 0
    max_num = 0

    temp = []

    for i in arr:
        temp.append(i)
    min_num = temp[0]

    #for producing max sum
    for i in range(0, 5):
        if(min_num >= arr[i]):
            min_num = arr[i]

    for i in range(0, 5):
        if(arr[i] == min_num):
            pass
        else:
            max_list.append(arr[i])

    for i in range(0, 4):
        max_sum += max_list[i]

    #for producing min sum
    for i in range(0, 5):
        if(max_num <= arr[i]):
            max_num = arr[i]
        # else:
        #     max_num = arr[temp]

    for i in range(0, 5):
        if(arr[i] == max_num):
            pass
        else:
            min_list.append(arr[i])

    for i in range(0, 4):
        min_sum += min_list[i]

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = []

    for i in range(0, 5):
        item = int(input())
        arr.append(item)

    miniMaxSum(arr)
