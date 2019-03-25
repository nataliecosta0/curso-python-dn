from unittest import TestCase
from app import my_languages


class TestIsDivisible(TestCase):
    def test_1(self):
        self.assertEqual(my_languages({"Java": 10, "Ruby": 80, "Python": 65}), ["Ruby", "Python"])

    def test_2(self):
        self.assertEqual(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}), ['Hindi', 'Dutch', 'Greek'])

    def test_3(self):
        self.assertEqual(my_languages({"C++": 50, "ASM": 10, "Haskell": 20}), [])


