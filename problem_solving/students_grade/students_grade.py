#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    new_list = []
    for i in range(0, len(grades)):
        if(grades[i] < 38):
            new_list.append(grades[i])
        else:
            temp = 0
            if((grades[i] + 1)%5 == 0 or (grades[i] + 2)%5 == 0):
                temp = int(round(grades[i]*2, -1)/2)
                new_list.append(temp)
            else:
                new_list.append(grades[i])

    print(new_list)
    return new_list

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "C://Users//taha_//Desktop//Hacker_rank//output.txt"
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input())

    grades = []

    for i in range(0, n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(str(result)))
    fptr.write('\n')

    fptr.close()
