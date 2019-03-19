'''
Problema #4
Crie sua primeira suite de testes para a classe da calculadora.
'''

from unittest import TestCase, main 

class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x + y

    def multi(self, x, y):
        return x + y

    def div(self, x, y):
        return x + y

class TestCalc(TestCase):
    def teste_da_soma(self):
        c = Calc()
        self.assertEqual(c.add(1, 2), 3, 'Errado')
