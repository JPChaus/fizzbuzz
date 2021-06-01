import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_printNum(self):
        self.assertEqual(fizzbuzz.printValue(1), 1)

    def test_printFizz(self):
        self.assertEqual(fizzbuzz.printValue(3), "Fizz")

    def test_printFizz(self):
        self.assertEqual(fizzbuzz.printValue(5), "Buzz")

if __name__ == '__main__':
    unittest.main()