from course import Course

class School:
    """ School Class - Maintians the details of a school """

    def __init__(self, school_name):

        School._validate_string_input("School Name", school_name)
        self._school_name = school_name

        self._courses = []

    def add_course(self, course):
        School._validate_string_input("Course", course)

        if not self.course_exists(course):
            self._courses.append(course)

    def course_exists(self, course_name):
        School._validate_string_input("Course name", course_name)

        if self._courses.count(course_name) > 0:
            return True

        return False

#    def remove_course(self, course_name):


#    def get_course(self, course_name):





    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")