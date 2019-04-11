'''
Problema #8 - use mocks
Baseado em ATDD e no fato de que existe uma função chamada
‘sabores_de_pizza’ que nos retorna uma tupla com (‘sabor’, ‘preço’: float) faça
uma função que recebe um valor: float e nos retorna as pizzas com preço <= ao
valor passado
'''

from unittest import TestCase, mock

def sabores_de_pizza():
    ...

def pizza_menor_preco(preco_maximo):
    return list(filter(lambda x: x[1] <= preco_maximo, sabores_de_pizza()))
    
#print(pizza_menor_preco(sabores_de_pizza))

class Test_sabores_pizza(TestCase):

    def teste_deve_retornar_pizza_com_valor_menor_ou_igual_ao_valor_passado(self):
        with mock.patch('teste_ex_8.sabores_de_pizza') as mocked_sabores_de_pizza:
            mocked_sabores_de_pizza.return_value = [('Calabresa', 40.00), ('Queijo', 30.00), ('Milho', 25.00), ('Baiana', 32.00), ('Portuguesa', 35.00)]

            self.assertEqual(pizza_menor_preco(30.00), [('Queijo', 30.00), ('Milho', 25.00)])