'''
Problema #6
Agora que você tem os testes para garantir o comportamaento dos seus métodos.
Você poderia efeuar a correção da classe sem grandes problemas?
'''

from unittest import TestCase

class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class ClasseTesteSoma(TestCase):
    def resultado_soma(self):
        c = Calc()
        entrada =  c.add(1, 1)
        resultado_esperado = 2
        self.assertEqual(entrada, resultado_esperado)

class ClasseTesteSub(TestCase):
    def resultado_sub(self):
        c = Calc()
        entrada = c.sub(1, 1)
        resultado_esperado = 0
        self.assertEqual(entrada, resultado_esperado)

class ClasseTesteMult(TestCase):
    def resultado_mult(self):
        c = Calc()
        entrada = c.mult(2, 2)
        resultado_esperado = 4
        self.assertEqual(entrada, resultado_esperado)

class ClasseTesteDiv(TestCase):
    def resultado_div(self):
        c = Calc()
        entrada = c.div(6, 2)
        resultado_esperado = 3
        self.assertEqual(entrada, resultado_esperado)