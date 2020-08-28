import unittest
from src.people.giulia.numbers import *


class TestNumbers(unittest.TestCase):

    def test_is_a_prime_number(self):
        self.assertTrue(is_a_prime_number(3709))
        self.assertFalse(is_a_prime_number(10000))
        self.assertTrue(is_a_prime_number(7919))

    def test_fib(self):
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(17), 1597)
        self.assertEqual(fib(23), 28657)

    def test_prime_number_fib(self):
        self.assertFalse(prime_number_fib(11), -1)
        self.assertTrue(prime_number_fib(23), 28657)
        self.assertFalse(prime_number_fib(22), 17711)

    def test_area(self):
        def test_circle_area():
            self.assertTrue(area(0, 7.8), 191.134497044)
            self.assertTrue(area(0, 10.97), 378.062087366)
            self.assertTrue(area(0, 1234.76), 4789773.4999)

        def test_triangle_area():
            self.assertTrue(area(1, 8.765, 7.999), 35.0556175)
            self.assertTrue(area(1, 9776.0006, 1122.055), 5484605.17662)

        def test_square_area():
            self.assertTrue(area(2, 987.7666), 975682.856076)
            self.assertTrue(area(2, 10294.0333), 105967121.582)

        test_circle_area()
        test_triangle_area()
        test_square_area()

