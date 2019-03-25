'''
Problema #5
Faça um programa que itere em uma lista de maneira imperativa e que armazene
em uma nova lista seu valor processado por uma função.
EX:
entrada = [‘foo’, ‘bar’, ‘spam’, ‘eggs’]
função = f(x) = x * 2
saida = [‘foofoo’, ‘barbar’, ‘spamspam’, ‘eggseggs’]
'''

from unittest import TestCase

listaEntrada = ['foo', 'bar', 'spam', 'eggs']
listaSaida = []

def multi(listaEntrada):
    for x in listaEntrada:
        listaSaida.append(x*2)
    return listaSaida

print(multi(listaEntrada))

class Teste(TestCase):
    def teste_multiplica(self):
        self.assertEqual(multi([listaEntrada]), ['foofoo', 'barbar', 'spamspam', 'eggseggs'])

