
import unittest
from main import students, register_student


class TestStudentRegistration(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_valid_registration(self):
        success, message = register_student(
            "ST001", "Ada Okafor", "20"
        )

        self.assertTrue(success)
        self.assertEqual(
            students["ST001"],
            {"name": "Ada Okafor", "age": 20}
        )

    def test_duplicate_id(self):
        register_student("ST001", "Ada Okafor", "20")

        success, message = register_student(
            "ST001", "John Musa", "24"
        )

        self.assertFalse(success)
        self.assertEqual(students["ST001"]["name"], "Ada Okafor")

    def test_invalid_age(self):
        success, message = register_student(
            "ST002", "Mary James", "-5"
        )

        self.assertFalse(success)
        self.assertNotIn("ST002", students)

    def test_non_integer_age(self):
        success, message = register_student(
            "ST003", "Peter James", "abc"
        )

        self.assertFalse(success)
        self.assertNotIn("ST003", students)


if __name__ == "__main__":
    unittest.main()
