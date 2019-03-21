'''
Problema #3
Agora é sua vez.
Usando TDD, desenvolva uma função que conte frequência de letras em uma
string
'''

from unittest import TestCase
from collections import Counter

def contador_letras(letras):
    if type(letras) == type(str):
        return conter(letras)

class Teste_letras(TestCase):
    def teste_contar_letras_iguais(self):
        self.assertEqual('123mudar')