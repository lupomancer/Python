#! /usr/bin/env python3

import os
import re
import sys
def get_student_avg(student_data):
    i = 0
    while i <= len(student_data) - 1:
        rawstudent = []
        rawstudent = student_data[i]
        tobeused = []
        tobeused = rawstudent.split()
        student_num = tobeused[0]
        ACIT1420 = tobeused[1]
        ACIT1515 = tobeused[2]
        ACIT1620 = tobeused[3]
        ACIT1630 = tobeused[4]
        COMM1116 = tobeused[5]
        MATH1310 = tobeused[6]
        ORGB1100 = tobeused[7]
        student_avgs = {}
        student_avg = round((int(ACIT1420) + int(ACIT1515) + int(ACIT1620) + int(
            ACIT1630) + int(COMM1116) + int(MATH1310) + int(ORGB1100)) / 7)
        student_avgs.update({student_num: str(student_avg)})
        f = open("student_avgs.txt", "a")
        f.write(student_num + ': ' + student_avgs[student_num] + '\n')
        print(student_avgs)
        i += 1

def get_course_avg():
    i = 0
    while i <= len(student_data) - 1:
        rawstudent = []
        rawstudent = student_data[i]
        tobeused = []
        tobeused = rawstudent.split()
        student_num = tobeused[0]
        ACIT1420 = tobeused[1]
        ACIT1515 = tobeused[2]
        ACIT1620 = tobeused[3]
        ACIT1630 = tobeused[4]
        COMM1116 = tobeused[5]
        MATH1310 = tobeused[6]
        ORGB1100 = tobeused[7]
        ACIT1420list = []
        ACIT1515list = []
        ACIT1620list = []
        ACIT1630list = []
        COMM1116list = []
        MATH1310list = []
        ORGB1100list = []
        ACIT1420list.append(ACIT1420)
        ACIT1515list.append(ACIT1515)
        ACIT1620list.append(ACIT1620)
        ACIT1630list.append(ACIT1630)
        COMM1116list.append(COMM1116)
        MATH1310list.append(MATH1310)
        ORGB1100list.append(ORGB1100)
        ACIT1420avg = sum(int(ACIT1420list))
        ACIT1515avg = sum(int(ACIT1515list))
        ACIT1620avg = sum(int(ACIT1620list))
        ACIT1630avg = sum(int(ACIT1630list))
        COMM1116avg = sum(int(COMM1116list))
        MATH1310avg = sum(int(MATH1310list))
        ORGB1100avg = sum(int(ORGB1100list))
        # I was going to take the average and then write it to the file
        i +=1
    j = 0
    

def main():
    try:
        grade_dir = sys.argv[1]
    except:
        print('Please enter a valid file name to process:')
        grade_dir = input()
    with open(grade_dir) as grade_file:
        student_data = []
        student_data = grade_file.readlines()
        del student_data[0]
        print(len(student_data))
        get_student_avg(student_data)

if __name__ == "__main__":
    main()
