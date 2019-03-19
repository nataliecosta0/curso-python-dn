'''
Problema #11
Usando a função ‘exp’ criada no problema 8. Faça a checagem dos inputs
indiretos da função de soma em um teste. Em outro teste faça a função dos inputs
indiretos da função de sub.
'''

from unittest import mock, TestCase

class TestCalc(TestCase):
    def test_input_indireto_soma(self):
        with mock.patch('calc.add') as spy:
            exp(1, 2, 3)

        spy.assert_called_with(1, 2)