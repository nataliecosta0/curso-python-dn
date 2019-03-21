'''
Problema #3
Agora é sua vez.
Usando TDD, desenvolva uma função que conte frequência de letras em uma
string
'''

from unittest import TestCase
from collections import Counter

def contar_letras(texto):
    return Counter(texto)

class TestContar(TestCase):
    def test_contar_letras(self):
        self.assertEqual(contar_letras('Oi'), {'O': 1, 'i': 1})