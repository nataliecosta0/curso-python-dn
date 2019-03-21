'''
Problema #2
Me guiem usando TDD para desenvolvermos esse cenário
'''

from unittest import TestCase

'''
def sub(x, y):
    try:
        return x - y
    except TypeError:
        return 'Não é um número'

def soma(x, y):
    try:
        return x + y
    except TypeError:
        return 'Não é um número'
'''

def exp(x, y, z):
    return sub(soma(x, y), z)

class TestSoma(TestCase):
    def test_soma_deve_retornar_2_com_1_1(self):
        self.assertEqual(soma(1, 1), 2)
    
    def test_soma_deve_retornar_11_com_1_1(self):
        self.assertEqual(soma('1', '1'), '11')
        
    def test_soma_deve_retornar_nao_e_numero_com_4_e_eduardo(self):
        self.assertEqual(soma(4, 'eduardo'), 'Não é um número')

class Testsub(TestCase):
    def test_sub_deve_retornar_0_com_1_1(self):
        self.assertEqual(sub(1, 1), 0)

    def test_sub_deve_retornar_0_com_1__1(self):
        self.assertEqual(sub(1, -1), 2)

class TestExp(TestCase):
    def test_exp(self):
        self.assertEqual(exp(1, 1, 1), 1)

    def test_exp_2(self):
        self.assertEqual(exp(lambda x: x + 1, [], 'eduardo'), None)