'''
Problema #8
Agora que você já contruiu a função ‘exp’ que tal fazer uma chamada de uma
expressão mais complexa?
f(x, y, z) -> exp(exp(x, y, z), y, z)
Agora tente efetuar os testes dessa função
'''

from unittest import TestCase

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x, y), z)

def funcaoNova(x, y, z):
    return exp(exp(x, y, z), y, z)

class TesteExpre(TestCase):

    def teste_1(self):
       self.assertEqual(funcaoNova(2, 2, 4), -2)

    def teste_2(self):
        self.assertEqual(funcaoNova(5, 5, 10), -5)

    