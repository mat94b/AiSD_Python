import unittest

from fracs import *


class Test(unittest.TestCase):
    def setUp(self):
        self.zero = [4, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([10, 1], [3, 3]), [11, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2, 6], [1, 3]), [0, 1])
        self.assertEqual(sub_frac([2, 1], [2, 1]), [0, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 1], [1, 1]), [1, 1])
        self.assertEqual(mul_frac([1, 2], [2, 1]), [1, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([4, 1], [2, 1]), [2, 1])
        self.assertEqual(div_frac([100, 2], [2, 1]), [25, 1])

    def test_is_positive(self):
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([3, -4]))
        self.assertTrue(is_positive([500,1000]))
        self.assertTrue(is_positive([-1, -1]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([1, 3]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [5, 10]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 5]), 0.2)
        self.assertEqual(frac2float([1, 2]), 0.5)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
