import unittest
from math import sum

class MathTestCase(unittest.TestCase):

    def test_sum(self):
        result = sum(10, 10)
        self.assertEqual(result, 20)

    def test_sum2(self):
        result = sum(11, 11)
        self.assertEqual(result, 22)

if __name__=='__main__':
    unittest.main()
