import unittest

from server import job_sum, job_product


class Testing(unittest.TestCase):

    def test_product_1(self):
        x = job_product([3,])
        self.assertEqual(x, 3)

    def test_product_2(self):
        x = job_product([1, 0.1, 5, 11621.5, 0.5, -4, -0.3])
        self.assertEqual(x, 3486.45)

    def test_product_fail_str(self):
        with self.assertRaises(ValueError):
            x = job_product([1, "abc"])

    def test_sum_1(self):
        x = job_sum([3,])
        self.assertEqual(x, 3)

    def test_sum_2(self):
        x = job_sum([1, 0.1, 5, 11621.5, 0.5, -4, -0.3])
        self.assertEqual(x, 11623.800000000001)

    def test_sum_fail_str(self):
        with self.assertRaises(TypeError):
            x = job_sum([1, "abc"])


if __name__ == '__main__':
    unittest.main()
