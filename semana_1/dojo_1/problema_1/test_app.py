from unittest import TestCase
from app import reverse_worlds 

class TestReverseWorlds(TestCase):
    def teste_1(self):
        self.assertEqual(reverse_worlds('oi'), 'oi')

    def teste_2(self):
        self.assertEqual(reverse_worlds('Olá bb'), 'bb Olá')

    def teste_3(self):
        self.assertEqual(reverse_worlds('voadoras Batatinhas'), 'Batatinhas voadoras')