'''
Exercício #1
Faça uma função que sofra efeito colateral por uma variável global. Após isso
responda se é possível criar um teste para ela.
'''

from unittest import TestCase

val = 1

def soma(x):
    return x + val

val = 2

class Test_funcao(TestCase):
    def test_deve_retornar_3(self):
        self.assertAlmostEqual(soma(2), 3)
