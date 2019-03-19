class Course:
    """ Course Class - Maintains the details of a course """

    def __init__(self, course_id, crn, program):
        """ Constructor - Initializes the main attributes of a student """

        Course._validate_string_input("Course ID", course_id)
        self._course_id = course_id

        Course._validate_string_input("CRN", crn)
        self._crn = crn

        Course._validate_string_input("Program", program)
        self._program = program

        self._student_ids = []

    def get_course_id(self):
        """ Returns the course ID """
        return self._course_id

    def get_crn(self):
        """ Returns the course CRN """
        return self._crn

    def get_program(self):
        """ Returns the program the course belongs to """
        return self._program

    def add_student(self, student_id):
        """ Adds a student to the course. Rejects duplicate students. """
        Course._validate_string_input("Student ID", student_id)

        if not self.is_enrolled_in_course(student_id):
            self._student_ids.append(student_id)

    def remove_student(self, student_id):
        """ Removes a student from a course """

        Course._validate_string_input("Student ID", student_id)

        if self.is_enrolled_in_course(student_id):
           self._student_ids.remove(student_id)

    def is_enrolled_in_course(self, student_id):
        """ Checks if a student is enrolled in the course """

        Course._validate_string_input("Student ID", student_id)

        if self._student_ids.count(student_id) > 0:
            return True

        return False

    def get_num_students(self):
        """ Returns the number of students enrolled in the course """
        return len(self._student_ids)

    def get_details(self):
        """ Returns the course details in a printable format """
        student_list = "None"

        if len(self._student_ids) > 0:
            student_list = ', '.join(str(x) for x in self._student_ids)

        details = self._course_id + " (" + self._crn + ") is a course in the " + self._program + \
                  " Program with the following students: " + student_list

        return details

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")
