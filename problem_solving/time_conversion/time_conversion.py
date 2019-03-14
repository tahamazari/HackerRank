#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    temp = 0
    for i in range(0, 10):
        if(s[8] == "P"):
            temp = s[0:2]
            temp = int(temp)
            temp = temp + 12
            if(temp == 24):
                temp = temp - 12
                temp = str(temp)
                military = "".join((temp, s[2:8]))
            else:
                temp = str(temp)
                military = "".join((temp, s[2:8]))

        elif(s[8] == "A"):
            temp = s[0:2]
            temp = int(temp)
            x = temp
            temp = temp - 12
            if(temp < 0):
                temp = x
                temp = str(temp)
                military = "".join((temp, s[2:8]))
                military = "".join(("0", military))
            else:
                temp = str(temp)
                military = "".join((temp, s[2:8]))
                military = "".join(("0", military))

    print(military)

    return military

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
