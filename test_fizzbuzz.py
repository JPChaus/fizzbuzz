import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_printNum(self):
        self.assertEqual(fizzbuzz.printValue(1), 1)

if __name__ == '__main__':
    unittest.main()