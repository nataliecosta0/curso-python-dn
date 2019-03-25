from unittest import TestCase
from app import is_divisible

class TestIsDivisible(TestCase):
    def test_1(self):
        self.assertEqual(is_divisible(3, 3, 4), False)

    def test_2(self):
        self.assertEqual(is_divisible(12, 3, 4), True)

    def test_3(self):
        self.assertEqual(is_divisible(8, 3, 4), False)

    def test_4(self):
        self.assertEqual(is_divisible(48, 3, 4), True)