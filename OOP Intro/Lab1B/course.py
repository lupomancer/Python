#!/usr/bin/env python3

class Course:
    """Course Class Desc"""

    def __init__(self, course_id, crn, school, program):
        """Constructs the Course object"""
        self._course_id = course_id
        self._crn = crn
        self._school = school
        self._program = program
        self._students = []

    def check(self, student_id):
        """Checks if a student ID already exists within the _students list"""
        if student_id in self._students:
            return True
        else:
            return False

    def remove(self, student_id):
        """removes a student based on ID if it exists within the _students list"""
        if self.check(student_id) == True:
            self._students.remove(student_id)

    def add(self, student_id):
        """adds a student based on ID if it doesn't already exist within the _students list"""
        if self.check(student_id) == False:
            self._students.append(student_id)

    def details(self):
        """prints out the details of a course with a list of all students, printing "none" if there are no students registered"""
        student_list = ", ".join(self._students)
        if len(self._students) == 0:
            student_list = "None"
        print(self._course_id, "(CRN " + self._crn + ") is a course in the", self._program, "program in the School of", self._school, "with the following students:", student_list)
