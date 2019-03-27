'''
Problema #8 - use mocks
Baseado em ATDD e no fato de que existe uma função chamada
‘sabores_de_pizza’ que nos retorna uma tupla com (‘sabor’, ‘preço’: float) faça
uma função que recebe um valor: float e nos retorna as pizzas com preço <= ao
valor passado
'''

from unittest import TestCase

def sabores_de_pizza():
    return [('Calabresa', 40,00),
            ('Queijo', 30,00),
            ('Milho', 25,00 ),
            ('Baiana', 32,00 ),
            ('Portuguesa', 35,00 )]

def menor_valor(valor):
    return list(filter(lambda x: x[1] <= ))