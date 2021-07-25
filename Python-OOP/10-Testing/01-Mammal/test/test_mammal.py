from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal('TestName', 'TestType', 'TestSound')

    def test_mammal_initialized(self):
        self.assertEqual(self.mammal.name, 'TestName')
        self.assertEqual(self.mammal.type, 'TestType')
        self.assertEqual(self.mammal.sound, 'TestSound')

    def test_mammal__make_sound(self):
        expected_result = "TestName makes TestSound"
        result = self.mammal.make_sound()
        self.assertEqual(expected_result, result)

    def test_kingdom_initialized(self):
        expected_result = "animals"
        result = self.mammal._Mammal__kingdom
        self.assertEqual(result, expected_result)

    def test_mammal__get_kingdom(self):
        expected_result = "animals"
        result = self.mammal.get_kingdom()
        self.assertEqual(expected_result, result)

    def test_mammal__info(self):
        expected_result = "TestName is of type TestType"
        result = self.mammal.info()
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

