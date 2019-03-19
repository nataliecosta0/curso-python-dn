'''
Problema #9
Usando a função ‘exp’ criada no problema 7. Teste a validação indireta da função
de soma usando um dummy
'''
from unittest import TestCase, main 

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x,y),z)

class TesteExpre(TestCase):
    dummy = 0
    def teste_soma(self):
        self.assertEqual(exp(self.dummy, self.dummy, 4), -4)