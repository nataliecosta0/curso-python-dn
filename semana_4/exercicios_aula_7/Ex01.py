'''
Exercício #1
Faça uma função que sofra efeito colateral por uma variável global. Após isso
responda se é possível criar um teste para ela.
'''

from unittest import TestCase

x = 1

def funcaoVaria(x):
    return x + 2

print(funcaoVaria(2))

x = 2

print(funcaoVaria(x))

class TesteFuncaoVaria(TestCase):
    def teste_funcao_variavel_retorna_4(self):
        self.assertEqual(funcaoVaria(x), 4)

    '''def teste_funcao_variavel_retorna_3(self):
        self.assertEqual(funcaoVaria(x), 3)'''

