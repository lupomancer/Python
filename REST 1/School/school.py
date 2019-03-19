from course import Course


class School:
    """ School with Courses """

    SCHOOL_NAME_LABEL = "School Name"
    COURSE_ID_LABEL = "Course ID"
    COURSE_LABEL = "Course"
    PROGRAM_NAME_LABEL = "Program Name"

    def __init__(self, school):
        """ Initializes the School with a Name """

        School._validate_string_input(School.SCHOOL_NAME_LABEL, school)
        self._school = school
        self._courses = []

    def get_school_details(self):
        """Creates a list of unique program names and returns all school details
        
        Returns:
            dictionary -- school details
        """

        programs = []
        program_list = []
        for course in self._courses:
            program_list.append(course.get_program())
        programs = list(set(program_list))

        dict = {}
        dict['school_name'] = self._school
        dict['num_courses'] = len(self._courses)
        dict['programs'] = programs

        return dict


    def add_course(self, course):
        """ Adds a Course to the School """

        School._validate_course_input(School.COURSE_LABEL, course)
        if course not in self._courses:
            self._courses.append(course)

    def get_all_courses(self):
        return self._courses

    def remove_course(self, course_id):
        """ Removes a Course from the School """

        School._validate_string_input(School.COURSE_ID_LABEL, course_id)
        for curr_course in self._courses:
                if curr_course.get_course_id() == course_id:
                    self._courses.remove(curr_course)
                    return

    def get_num_courses(self):
        """ Gets the Number of Courses """

        return len(self._courses)

    def course_exists(self, course_id):
        """ Checks if the Course exists in the School """

        School._validate_string_input(School.COURSE_ID_LABEL, course_id)
        for course_check in self._courses:
            if course_check.get_course_id() == course_id:
                return True

        return False

    def get_num_courses_in_program(self, program):
        """ Returns the number of Courses in the Program """

        School._validate_string_input(School.PROGRAM_NAME_LABEL, program)
        counter = 0
        for count_course in self._courses:
            if program in count_course.get_details():
                counter += 1
        return counter

    def get_course(self, course_id):
        """ Gets the Course with the given Course ID """

        School._validate_string_input(School.COURSE_ID_LABEL, course_id)
        for course in self._courses:
            if course.get_course_id() == course_id:
                return course

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")
        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_course_input(display_name, obj_value):
        """ Private helper to validate course values """

        if obj_value is None:
            raise ValueError(display_name + " must be defined.")

