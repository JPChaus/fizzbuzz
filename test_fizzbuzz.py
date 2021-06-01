import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_printNum(self):
        self.assertEqual(fizzbuzz.printValue(1), 1)

    def test_printFizz(self):
        self.assertEqual(fizzbuzz.printValue(3), "Fizz")

if __name__ == '__main__':
    unittest.main()