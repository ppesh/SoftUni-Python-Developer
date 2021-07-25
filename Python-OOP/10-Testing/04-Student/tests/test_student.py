from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student('Asen')

    def test_student__initialized(self):
        result = [self.student.name, self.student.courses]
        expected_result = ['Asen', {}]
        self.assertListEqual(expected_result, result)

    def test_student__enroll_course_adding(self):
        msg = self.student.enroll('Math', [1, 2, 3], 'proba')
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {'Math': []}, 'Course has been added.']
        self.assertListEqual(expected_result, result)

    def test_student__enroll_if_course_name_in_course(self):
        self.student.enroll('Math', [1, 2, 3], 'proba')
        msg = self.student.enroll('Math', [1, 2, 3], 'proba')
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {'Math': [1, 2, 3]}, 'Course already added. Notes have been updated.']
        self.assertListEqual(expected_result, result)

    def test_student__enroll_if_add_course_notes_equal_Y(self):
        msg = self.student.enroll('Math', [1, 2, 3], 'Y')
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {'Math': [1, 2, 3]}, 'Course and course notes have been added.']
        self.assertListEqual(expected_result, result)

    def test_student__enroll_if_add_course_notes_equal_empty_str(self):
        msg = self.student.enroll('Math', [1, 2, 3], '')
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {'Math': [1, 2, 3]}, 'Course and course notes have been added.']
        self.assertListEqual(expected_result, result)

    def test_student__add_notes_method_if_course_name_in_course(self):
        self.student.enroll('Math', [1, 2, 3], 'kjhkj')
        msg = self.student.add_notes('Math', [1, 2, 3])
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {'Math': [[1, 2, 3]]}, 'Notes have been updated']
        self.assertListEqual(expected_result, result)

    def test_student__add_notes_method_if_course_name_not_in_course(self):
        with self.assertRaises(Exception):
            self.student.add_notes('Math', [1, 2, 3])

    def test_student__leave_course_method_if_course_name_in_course(self):
        self.student.enroll('Math', [1, 2, 3], 'kjhkj')
        msg = self.student.leave_course('Math')
        result = [self.student.name, self.student.courses, msg]
        expected_result = ['Asen', {}, 'Course has been removed']
        self.assertListEqual(expected_result, result)

    def test_student__leave_course_method_if_course_name_not_in_course(self):
        with self.assertRaises(Exception):
            self.student.leave_course('Math')


if __name__ == "__main__":
    main()
