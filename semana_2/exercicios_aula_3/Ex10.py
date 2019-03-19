'''
Problema #10
Usando a função ‘exp’ criada no problema 8. Teste a validação indireta da função
de subtração usando um dummy
'''
from unittest import TestCase, main 

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x,y),z)

class TesteExpre(TestCase):
    dummy = 3
    def teste_sub(self):
        self.assertEqual(exp(2, 5, self.dummy), 4)

    def teste_sub2(self):
        self.assertEqual(exp(2, 1, self.dummy), 0)

    def teste_sub3(self):
        self.assertEqual(exp(8, 2, self.dummy), 7)