'''
Problema #4
Crie sua primeira suite de testes para a classe da calculadora.
'''

from unittest import TestCase

class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x + y
    
    def mult(self, x, y):
        return x + y

    def div(self, x, y):
        return x + y

class ClasseTeste(TestCase):
    def resultado_soma(self):
        c = Calc()

        self.assertEqual(c.add(1, 1), 2)