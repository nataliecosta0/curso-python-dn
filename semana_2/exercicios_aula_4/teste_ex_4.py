'''
Problema #4
Crie uma função que recebe uma string e a transforma em uma lista:
‘Python’ -> [‘Python’]
‘Python love’ -> [‘Python’, ‘love’]
‘Python é foda’ -> [‘Python’, ‘é’, ‘foda’]
lembre-se, TDD
'''

from unittest import TestCase

def funcao_retorna(texto):
    resultado = texto.split(' ')
    return resultado

class Teste_lista(TestCase):
    def teste_metodo_retornar(self):
        self.assertEqual(funcao_retorna('Python'), ['Python'])

    def teste_retorna_python_love(self):
        self.assertEqual(funcao_retorna('Python love'), ['Python', 'love'])