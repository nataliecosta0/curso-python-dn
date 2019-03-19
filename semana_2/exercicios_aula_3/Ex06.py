'''
Problema #6
Agora que você tem os testes para garantir o comportamaento dos seus métodos.
Você poderia efeuar a correção da classe sem grandes problemas?
'''

from unittest import TestCase, main

class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multi(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class TestSoma(TestCase):
    def teste_soma(self):
        c = Calc()
        self.assertEqual(c.add(1, 2), 3, 'Errado')
        self.assertEqual(c.add(2, 2), 4, 'Errado')

    def teste_subtra(self):
        c = Calc()
        self.assertEqual(c.sub(1, 1), 0, 'Errado')
        self.assertEqual(c.sub(4, 2), 2, 'Errado')

    def teste_multi(self):
        c = Calc()
        self.assertEqual(c.multi(2, 2), 4, 'Errado')
        self.assertEqual(c.multi(6, 6), 36, 'Errado')
        self.assertEqual(c.multi(6, 2), 12, 'Errrado')

    def teste_div(self):
        c = Calc()
        self.assertEqual(c.div(10, 2), 5, 'Errado')
        self.assertEqual(c.div(8, 2), 4, 'Errado')
