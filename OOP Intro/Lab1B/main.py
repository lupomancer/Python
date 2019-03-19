#! /usr/bin/env python3

from course import Course

def main():
    #testing out the course class

    ACIT2515 = Course("ACIT2515", "12345", "Computing", "CIT")
    ACIT2515.add("A01048668")
    ACIT2515.add("A00000001")
    ACIT2515.add("A00000002")
    ACIT2515.remove("A01048668")
    if (ACIT2515.check("A01048668") == False):
        print("I should be enrolled in ACIT 2515")
    ACIT2515.details()

    ACIT2520 = Course("ACIT2520", "54321", "Computing", "CIT")
    ACIT2520.add("A01048668")
    ACIT2520.add("A00000001")
    ACIT2520.add("A00000002")
    ACIT2520.add("A00000003")
    ACIT2520.add("A00000004")
    ACIT2520.remove("A00000001")
    ACIT2520.remove("A00000002")
    ACIT2520.remove("A00000003")
    ACIT2520.add("A01048668")
    ACIT2520.details()

    MATH1350 = Course("MATH1350", "11111", "Mathematics", "CIT")
    MATH1350.details()

if __name__ == "__main__":
    main()
