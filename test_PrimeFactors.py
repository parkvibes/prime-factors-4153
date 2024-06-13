from unittest import TestCase
from PrimeFactors import *


class Test(TestCase):
    def setUp(self):
        self.primeFactors = PrimeFactors()

    def test_get_prime_factors_1(self):
        self.assertEqual([], self.primeFactors.of(1))

    def test_get_prime_factors_2(self):
        self.assertEqual([2], self.primeFactors.of(2))

    def test_get_prime_factors_3(self):
        self.assertEqual([3], self.primeFactors.of(3))

    def test_get_prime_factors_4(self):
        self.assertEqual([2, 2], self.primeFactors.of(4))

    def test_get_prime_factors_6(self):
        self.assertEqual([2, 3], self.primeFactors.of(6))

    def test_get_prime_factors_9(self):
        self.assertEqual([3, 3], self.primeFactors.of(9))
