import unittest
from src.people.isa.numbers import *


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
