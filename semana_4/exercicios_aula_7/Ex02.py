'''
Exercício #2
Faça uma função que gere efeito colateral.
'''

from unittest import TestCase

val = 1

def funcao(x):
    global val
    val += 1 # val = val +1
    return x + val

class Test_funcao(TestCase):
    def test_deve_retornar_resultado_4(self):
        self.assertEqual(funcao(2),4)

    def test_deve_retornar_resultado_4_segundo(self):
        self.assertEqual(funcao(2),4)

