from unittest import TestCase
from PrimeFactors import *


class Test(TestCase):
    def test_get_prime_factors_1(self):
        p = PrimeFactors()
        self.assertEqual([], p.of(1))
