import unittest
from math import sum

class MathTestCase(unittest.TestCase):

    def test_sum(self):
        result = sum(10, 10)
        self.assertEqual(result, 30)

if __name__=='__main__':
    unittest.main()
