'''
Problema #9
Usando a função ‘exp’ criada no problema 7. Teste a validação indireta da função
de soma usando um dummy
'''
from unittest import TestCase, main 
from typing import NewType, Any

Dummy = NewType('Dummy', Any)

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x,y),z)

class TesteExpre(TestCase):
    dummy = 2
    def teste_soma(self):
        self.assertEqual(exp(self.dummy, self.dummy, 2), 2) #subs de soma

    def teste_soma2(self):
        self.assertEqual(exp(self.dummy, 1, 2), 1) #uma soma

    def teste_soma3(self):
        self.assertEqual(exp(0, 2, self.dummy), 0) #sub