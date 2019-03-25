'''
Problema #5
Usando as funções desenvolvidas nos problemas 4 e 5.
Crie uma função, que ao utilizar as duas faça uma contagem de frequência de
elementos em uma lista.
Lembre-se, só é possível testar o resultado sabendo dos inputs diretos e
indiretos.
'''

from unittest import TestCase
from collections import Counter

def funcao_retorna(texto):
    resultado = texto.split(' ')
    return resultado

def contar_letras(texto):
    return Counter(texto)

def frequencia(texto):
    return contar_letras(funcao_retorna(texto))

class TestFrequenciaLista(TestCase):
    def teste_retorna_quantidade_elementos(self):
        self.assertEqual(frequencia('Python'), {'Python': 1})

    def teste_retorna_quantidade_elementos_repetidos(self):
        self.assertEqual(frequencia('Python Python é love'), {'Python': 2, 'é': 1, 'love': 1})

    def teste_retorna_quantidade_elementos_nao_repetidos(self):
        self.assertEqual(frequencia('Python é love'), {'Python': 1, 'é': 1, 'love': 1})