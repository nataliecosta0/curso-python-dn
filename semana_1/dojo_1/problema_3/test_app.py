from unittest import TestCase
from app import longest


class TestIsDivisible(TestCase):
    def test_1(self):
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")

    def test_2(self):
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")

    def test_3(self):
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
