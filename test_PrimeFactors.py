from unittest import TestCase
from PrimeFactors import *


class Test(TestCase):
    def test_get_prime_factors_1(self):
        p = PrimeFactors()
        self.assertEqual([], p.of(1))

    def test_get_prime_factors_2(self):
        p = PrimeFactors()
        self.assertEqual([2], p.of(2))
