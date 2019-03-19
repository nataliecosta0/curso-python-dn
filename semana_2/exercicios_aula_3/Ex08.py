'''
Problema #8
Agora que você já contruiu a função ‘exp’ que tal fazer uma chamada de uma
expressão mais complexa?
f(x, y, z) -> exp(exp(x, y, z), y, z)
Agora tente efetuar os testes dessa função
'''

from unittest import TestCase, main 

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, x):
    return sub(soma(x, y), z)

def exp(x, y, z):
    return exp(exp(x, y, z), y, z)

class TesteExpre(TestCase):
    def teste(self):
        self.assertEqual(exp(exp(0, 0, 0), 0, 0))

        