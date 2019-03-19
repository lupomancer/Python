#! /usr/bin/env python3
"""
This module builds a program workload for a general interest computing
program.  Courses are selected from a course calendar.

Being a general interest continuing studies program and there are no program
requirements either in number of, ordering, or specific required courses.

Once a user has completed course selections. the total program hours are
calculated based on the number of credits in each course.  Each credit is
comprised of 14 hours of course work.

From the required hours the number of semesters is calculated based on a
semester length of 120 hours for part time studies and 360 hours for full time
studies.

The courses selected and the number of semesters required to finish the program
is printed for the user.

"""

import math

calendar = {
    "CS101": 6.00,
    "CS102": 6.00,
    "CS103": 5.00,
    "CS104": 5.00,
    "MA101": 4.00,
    "MA102": 4.00,
    "CO101": 3.00,
    "CO102": 3.00,
    "OR101": 3.00,
    "OR102": 3.00
}

def course_hours(course):
    """
    Calculate the number of hours to complete a given course

    Args:
        course (str): the name of the course

    Returns:
        (float): the number of hours required to complete the course
    """
    #Function body goes here
    hours = calendar[course] * 14
    return hours


def calculate_semesters(workload, attendance):
    """
    Calculates the number of semester to complete the courseload and attendance

    Based on the students delivery type ("pt" - Part Time or "ft" - Full Time)
    calculate the number of semesters to complete their workload.

    The number of hours in a course is calculated as follows:
        course hours = credits * 14 hours per credit

    The number of hours in a semester is specified as follows:
        pt = 120
        ft = 360

    The number of semesters is calculated as follows:
        (the total hours in program / hours in semester) rounded up to nearest
        whole semester.

    see 'math.ceil' for standard library method of performing rounding up

    Args:
        workload (List[str]): this is a list of course codes that comprise the
                              students workload

        attendance (str): "pt" or "ft" indicating whether the student will be
                          attending part time or full time

    Returns:
        int: number of semesters to complete workload
    """
    #Function body goes here
    i = 0
    for i in len(workload):
        hours = sum(course_hours(workload(i)))
        if attendance == 'ft':
            semesters = math.ceil(360/hours)
        if attendance == 'pt':
            semesters = math.ceil(120/hours)
    i += 1

    return semesters


def build_program():
    """
    Prompt the user for courses that they want to enroll in and add them to
    their customized program

    If the courses is not in the course catalogue inform them by printing:
        "Sorry, $course_input isn't currently offered"

    Where $course_input is the course code they entered at the prompt.

    After a failed input attempt the user will be prompted to input another course code.

    The user will continue to select courses until they enter 'done' when to
    indicate that have finished adding courses.

    Returns:
        (List[str]):  a list of courses to in which the student will be enrolled
    """

    course = ""
    program = []

    while course != "done":
        #body of processing loop
        course = input("What course would you like register for - enter 'done' when finished:")
        program.append(course)
        print("Your program includes the following courses:")
        print(program)
    return program


def main():
    """
    Build course program and select delivery type, then print the courses and
    completion time in semesters
    """

    #Function body goes here
    #You need to properly populate the following variables:
    #   delivery_type: prompt the user for the desired delivery type
    delivery_type = input("Will you be attending full time(ft) or part time (pt):")

    #   program: list of courses
    program = build_program()
    #   semesters: number of semesters to complete courses
    calculate_semesters(program, delivery_type)
    # Following outputs the courses in the program
    print("Your program includes the following courses:\n{}".format(program))

    # Following outputs the number of semesters
    print("It will take you {} semesters to complete".format(semesters))


if __name__ == "__main__":
    main()
