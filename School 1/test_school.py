from unittest import TestCase
from school import School
from course import Course


class TestSchool(TestCase):
    """ Unit Tests for the School Class """

    def test_school(self):
        """ 010A - Valid Construction """

        test_school = School("Computing and Academic Studies")
        self.assertIsNotNone(test_school, "School must be defined")

    def test_school_invalid_parameters(self):
        """ 010B - Invalid Construction Parameters """

        # Must reject an undefined school name
        undefined_school = None
        self.assertRaisesRegex(ValueError, "School Name cannot be undefined", School, undefined_school)

        # Must reject an empty school name
        empty_school = ""
        self.assertRaisesRegex(ValueError, "School Name cannot be empty.", School, empty_school)

    def test_add_course(self):
        """ 020A - Valid Add Course """
        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        self.assertEqual(test_school.get_num_courses(), 0, "School must have no courses")

        test_school.add_course(test_course_1)
        self.assertEqual(test_school.get_num_courses(), 1, "School must have 1 course")

        test_school.add_course(test_course_2)
        self.assertEqual(test_school.get_num_courses(), 2, "School must have 2 courses")

    def test_add_course_undefined(self):
        """ 020B - Invalid Add Course Parameters """

        test_school = School("Computing and Academic Studies")

        invalid_course = None
        self.assertRaisesRegex(ValueError, "Course must be defined.", test_school.add_course, invalid_course)

    def test_add_course_already_exists(self):
        """ 020C - Course Already Exists """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_school = School("Computing and Academic Studies")
        self.assertEqual(test_school.get_num_courses(), 0, "School must have no courses")

        test_school.add_course(test_course_1)
        self.assertEqual(test_school.get_num_courses(), 1, "School must have 1 course")

        # Add the same course again
        test_school.add_course(test_course_1)
        self.assertEqual(test_school.get_num_courses(), 1, "School must still have only 1 course")

    def test_course_exists(self):
        """ 030A - Valid Course Exists """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        self.assertTrue(test_school.course_exists("ACIT2515"), "Course ACIT2515 must exist")
        self.assertTrue(test_school.course_exists("COMP1510"), "Course COMP1510 must exist")

    def test_course_exists_invalid_course_id(self):
        """ 030B - Invalid Course ID Exists Parameters """

        test_school = School("Computing and Academic Studies")

        course_id_undef = None
        self.assertRaisesRegex(ValueError, "Course ID cannot be undefined.", test_school.course_exists, course_id_undef)

        course_id_empty = ""
        self.assertRaisesRegex(ValueError, "Course ID cannot be empty.", test_school.course_exists, course_id_empty)

    def test_course_exists_not_existent_course(self):
        """ 030C - Valid Course Does Not Exist """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        self.assertFalse(test_school.course_exists("ACIT1234"), "Course ACIT1234 must NOT exist")
        self.assertFalse(test_school.course_exists("COMP4321"), "Course4321 must NOT exist")

    def test_remove_course(self):
        """ 040A - Valid Remove Course """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        self.assertEqual(test_school.get_num_courses(), 2, "School must have 2 courses")
        self.assertTrue(test_school.course_exists("ACIT2515"))
        self.assertTrue(test_school.course_exists("COMP1510"))

        test_school.remove_course("ACIT2515")
        self.assertEqual(test_school.get_num_courses(), 1, "School must have 1 course")
        self.assertFalse(test_school.course_exists("ACIT2515"))

    def test_remove_course_invalid_course_id(self):
        """ 040B - Invalid Remove Course Parameters """

        test_school = School("Computing and Academic Studies")

        course_id_undef = None
        self.assertRaisesRegex(ValueError, "Course ID cannot be undefined.", test_school.remove_course, course_id_undef)

        course_id_empty = ""
        self.assertRaisesRegex(ValueError, "Course ID cannot be empty.", test_school.remove_course, course_id_empty)

    def test_remove_non_existent_course(self):
        """ 040C - Invalid Remove Course Non-Existent """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        self.assertEqual(test_school.get_num_courses(), 2, "School must have 2 courses")
        self.assertTrue(test_school.course_exists("ACIT2515"))
        self.assertTrue(test_school.course_exists("COMP1510"))

        test_school.remove_course("ACIT1234")
        self.assertEqual(test_school.get_num_courses(), 2, "School must have 2 courses")

    def test_get_course(self):
        """ 050A - Valid Get Course """
        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        retrieved_course = test_school.get_course("ACIT2515")
        self.assertEqual(retrieved_course.get_course_id(), "ACIT2515", "Course must have course ID ACIT2515")
        self.assertEqual(retrieved_course.get_crn(), "123456", "Course must have CRN 123456")
        self.assertEqual(retrieved_course.get_program(), "CIT", "Course must be in CIT program")

    def test_get_course_invalid_course_id(self):
        """ 050B - Invalid Get Course Parameters """

        test_school = School("Computing and Academic Studies")

        course_id_undef = None
        self.assertRaisesRegex(ValueError, "Course ID cannot be undefined.", test_school.get_course, course_id_undef)

        course_id_empty = ""
        self.assertRaisesRegex(ValueError, "Course ID cannot be empty.", test_school.get_course, course_id_empty)

    def test_get_non_existent_course(self):
        """ 050C - Invalid Get Course Non-Existent """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A010000056")

        test_course_2 = Course("COMP1510", "456321", "CST")
        test_course_2.add_student("A010000056")
        test_course_2.add_student("A010450012")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)

        self.assertIsNone(test_school.get_course("ACIT1234"), "No course should exists for ACIT1234")

    def test_get_num_courses_in_program(self):
        """ 060A - Valid Get Number of Courses in Program """

        test_course_1 = Course("ACIT2515", "123456", "CIT")
        test_course_1.add_student("A01000056")

        test_course_2 = Course("COMP1409", "123444", "CSD")
        test_course_2.add_student("A01000056")

        test_course_3 = Course("COMP1510", "123555", "CSD")
        test_course_3.add_student("A01000045")

        test_course_4 = Course("COMP2530", "123667", "CSD")
        test_course_4.add_student("A01000034")

        test_school = School("Computing and Academic Studies")
        test_school.add_course(test_course_1)
        test_school.add_course(test_course_2)
        test_school.add_course(test_course_3)
        test_school.add_course(test_course_4)

        self.assertEqual(test_school.get_num_courses_in_program("CIT"), 1, "Must be only 1 CIT course")
        self.assertEqual(test_school.get_num_courses_in_program("CSD"), 3, "Must be 3 CSD courses")
        self.assertEqual(test_school.get_num_courses_in_program("SSD"), 0, "Must be no SSD courses")

    def test_get_num_courses_in_program_invalid_program_name(self):
        """ 060B - Invalid Get Num Course in Program Parameters """

        test_school = School("Computing and Academic Studies")

        program_name_undef = None
        self.assertRaisesRegex(ValueError, "Program Name cannot be undefined.", test_school.get_num_courses_in_program, program_name_undef)

        program_name_empty = ""
        self.assertRaisesRegex(ValueError, "Program Name cannot be empty.", test_school.get_num_courses_in_program, program_name_empty)

