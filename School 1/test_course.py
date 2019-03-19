from unittest import TestCase
from course import Course

class TestCourse(TestCase):
    """Unit Test for the Course Class"""

    def test_course(self):
        """TP-1A: valid construction"""
        course = Course("ACIT2515", "123456", "CIT")
        self.assertIsNotNone(course, "Course must be defined")

    def test_course_invalid_parameters(self):
        """TP-1B: check if any values in constructor are left 'None'"""
        course = Course("ACIT2515", "123456", "CIT")

        # Must reject undefined course parameters
        self.assertRaisesRegex(
            ValueError, "Course ID cannot be undefined.", Course, None, "123456", "CIT")
        self.assertRaisesRegex(
            ValueError, "CRN cannot be undefined.", Course, "ACIT2515", None, "CIT")
        self.assertRaisesRegex(
            ValueError, "Program cannot be undefined.", Course, "ACIT2515", "123456", None)

        """"TP-1C: check if any of the values in the constructor is empty"""
        # Must reject empty course parameters
        self.assertRaisesRegex(
            ValueError, "Course ID cannot be empty.", Course, "", "123456", "CIT")
        self.assertRaisesRegex(
            ValueError, "CRN cannot be empty.", Course, "ACIT2515", "", "CIT")
        self.assertRaisesRegex(
            ValueError, "Program cannot be empty.", Course, "ACIT2515", "123456", "")

    def test_get_course_id(self):
        """TP-2A: check if the get_course_id function is working"""
        # Must return CID entered
        course = Course("ACIT2515", "123456", "CIT")
        self.assertIsNotNone(course)
        self.assertEqual("ACIT2515", course.get_course_id(), "Course ID should be ACIT2515")

    def test_get_crn(self):
        """TP-3A: check if the get_crn function is working"""
        # Must return CRN entered
        course = Course("ACIT2515", "123456", "CIT")
        self.assertEqual(course.get_crn(), "123456")

    def test_get_program(self):
        """TP-4A: check if the get_program function is working"""
        # Must return program entered
        course = Course("ACIT2515", "123456", "CIT")
        self.assertEqual(course.get_program(), "CIT")

    def test_add_student_not_enrolled(self):
        """TP-5A: check if the add_student function is enrolling students properly"""
        course = Course("ACIT2515", "123456", "CIT")
        course.add_student("A01048668")
        self.assertTrue(course.is_enrolled_in_course("A01048668"))

    def test_add_student_already_enrolled(self):
        """TP-5B: check if the student already enrolled check works"""
        course = Course("ACIT2515", "123456", "CIT")
        course.add_student("A01048668")
        course.add_student("A01048668")

        self.assertEqual(course.get_num_students(), 1, "You cannot have two of the same student enrolled")

    def test_add_student_invalid(self):
        """TP-5C: check the validity of the student ID"""
        course = Course("ACIT2515", "123456", "CIT")
        student = "A01048668"
        self.assertIsNotNone(student)
        course.add_student(student)

        self.assertNotEqual(course.get_details(), "ACIT2515 (123456) is a course in the CIT Program with the following students: ", "Student ID cannot be undefined")

    def test_add_student_empty(self):
        """TP-5D: check if the student ID is empty"""
        course = Course("ACIT2515", "123456", "CIT")
        student = "A01048668"
        self.assertNotEqual(student, "")
        course.add_student(student)

        self.assertNotEqual(course.get_details(), "ACIT2515 (123456) is a course in the CIT Program with the following students: ", "Student ID cannot be empty")

    def test_remove_student_not_enrolled(self):
        """TP-6A: check if the student is not enrolled"""
        course = Course("ACIT2515", "123456", "CIT")
        course.remove_student("A01048668")
        self.assertFalse(course.is_enrolled_in_course("A01048668"))

    def test_remove_student_already_enrolled(self):
        """TP-6B: check if the student is removed properly"""
        course = Course("ACIT2515", "123456", "CIT")
        course.add_student("A01048668")
        course.remove_student("A01048668")
        self.assertFalse(course.is_enrolled_in_course("A01048668"))

    def test_remove_student_invalid(self):
        """TP-6C: check if the student ID is set to none"""
        course = Course("ACIT2515", "123456", "CIT")
        student = "A01048668"
        self.assertIsNotNone(student)
        course.add_student(student)
        course.remove_student(student)
        self.assertEqual(course.get_num_students(), 0, "Student ID cannot be undefined")

    def test_remove_student_empty(self):
        """TP-6D: check if the student ID is empty"""
        course = Course("ACIT2515", "123456", "CIT")
        student = "A01048668"
        self.assertNotEqual(student, "")
        course.add_student(student)
        course.remove_student(student)
        self.assertEqual(course.get_num_students(), 0, "Student ID cannot be empty")

    def test_is_enrolled_in_course_morethan0(self):
        """TP-7A: check if there are more than 0 students enrolled"""
        course = Course("ACIT2515", "123456", "CIT")
        student1 = "A00000001"
        student2 = "A00000002"
        student3 = "A00000003"
        course.add_student(student1)
        course.add_student(student2)
        course.add_student(student3)
        self.assertEqual(course.is_enrolled_in_course("A00000001"), True, "A00000001 should be enrolled")
        self.assertEqual(course.is_enrolled_in_course("A00000002"), True, "A00000002 should be enrolled")
        self.assertEqual(course.is_enrolled_in_course("A00000003"), True, "A00000003 should be enrolled")


    def test_is_enrolled_in_course_0(self):
        """TP-7B: check if there are 0 students enrolled"""
        course = Course("ACIT2515", "123456", "CIT")
        self.assertEqual(course.is_enrolled_in_course("A00000001"), False, "A00000001 shouldn't be enrolled")
        self.assertEqual(course.is_enrolled_in_course("A00000002"), False, "A00000002 shouldn't be enrolled")
        self.assertEqual(course.is_enrolled_in_course("A00000003"), False, "A00000003 shouldn't be enrolled")

    def test_is_enrolled_in_course_invalid(self):
        """TP-7C: check if the students enrolled are valid"""
        course = Course("ACIT2515", "123456", "CIT")

        student_undef = None
        self.assertRaisesRegex(ValueError, "Student ID cannot be undefined.",course.is_enrolled_in_course, student_undef)

        """TP-7D: check if the students enrolled isn't empty"""
        student_empty = ""
        self.assertRaisesRegex(ValueError, "Student ID cannot be empty.",course.is_enrolled_in_course, student_empty)

    def test_get_num_students(self):
        """TP-8A: check if the get_num_students method returns a valid number"""
        course = Course("ACIT2515", "123456", "CIT")
        student1 = "A00000001"
        student2 = "A00000002"
        student3 = "A00000003"
        course.add_student(student1)
        course.add_student(student2)
        course.add_student(student3)
        course.get_num_students
        self.assertEqual(course.get_num_students(), 3, "There should be 3 students enrolled")

    def test_get_details(self):
        """TP-9A: check the get_details function"""
        course = Course("ACIT2515", "123456", "CIT")
        student = "A01048668"
        course.add_student(student)
        self.assertNotEqual(course.get_details(), "ACIT2515 (123456) is a course in the CIT Program with the following students: ", "Course cannot be empty")