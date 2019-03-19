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
    return soma(sub(x,y),z)

class TesteExpre(TestCase):
    dummy = 0
    def teste_sub(self):
        self.assertEqual(exp(self.dummy, self.dummy, 4), 4)