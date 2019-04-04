'''
Exercício #3
Teste a função ‘diga_ola’ de maneira automatizada
'''

from unittest import TestCase, mock
import builtins

def diga_ola():
    nome = input('Me diga o seu nome: ')
    print(f'Ola {nome}')


class TestIO(TestCase):

    @mock.patch('builtins.input', return_value='Natalie')
    @mock.patch('builtins.print')

    def test_diga_ola_deve_digitar_algo(self, m_out, m_in):
        diga_ola()
        m_in.assert_called_with('Diga seu nome')
        m_out.assert_called_with('Olá Natalie')
