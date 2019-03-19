'''
Problema #7
Dada que exista uma função de soma e uma de subtração.
Crie uma função chamada ‘exp’ que receba x, y e z. E calcule:
f(x, y, z) -> x + y - z
Faça o teste dessa função, testando seus inputs e outputs indiretos
'''

from unittest import TestCase, main 

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x,y),z)

class TesteExpre(TestCase):
    def teste(self):
        self.assertEqual(exp(1, 2, 3), 0)




