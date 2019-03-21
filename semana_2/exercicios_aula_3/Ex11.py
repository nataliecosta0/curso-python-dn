'''
Problema #11
Usando a função ‘exp’ criada no problema 8. Faça a checagem dos inputs
indiretos da função de soma em um teste. Em outro teste faça a função dos inputs
indiretos da função de sub.
'''
 
from unittest import mock, TestCase

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x, y), z)

class TestarExp(TestCase):
    def test_exp_entrada_indireta_soma_recebe_xy(self):
        x = 2
        y = 3
        z = 4
        with mock.patch('Ex11.soma') as moked_soma:
            exp(x, y, z)

        moked_soma.assert_called_with(x, y)

    def test_exp_entrada_indireta_sub_recebe_z(self):
        with mock.patch('Ex11.sub') as moked_sub:
            exp(2, 3, 4)
        
        moked_sub.assert_called_with(5, 4)

