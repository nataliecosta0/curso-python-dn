'''
Problema #6 - use stubs
Sabendo que existe uma função ‘get_users’ que faz uma chamada no banco de
dados. Quando ela é chamada retorna uma lista de tuplas com os seguintes
valores:
(id, nome, email) -> (507, Jorge, jorgin_gatin@hotmail.com)
Faça uma função ‘filter_users’ onde serão retornados apenas os usuários com id
superior a 100.
'''

from unittest import TestCase

#lista_usuario = []
def get_users():
    return [(10, 'Matheus', 'matheus_ss@hotmail.com'),
                      (20, 'Lucas', 'lucas_ribeiro@hotmail.com'),
                      (140, 'Júlia', 'julia_sensacao@hotmail.com'),
                      (235, 'Marina', 'marina_s2@hotmail.com'),
                      (80, 'Gustavo', 'gustavo_fan@hotmail.com'),
                      (500, 'Bruna', 'bruna_costa@hotmail.com'),
                      (507, 'Jorge', 'jorgin_gatin@hotmail.com'),]

def filter_users(lista_usuario):
    return list(filter(lambda x: x[0]> 100, lista_usuario))

#print(get_users(lista_usuario))
#print(filter_users(lista_usuario))

class Test_funcao_filtrar(TestCase):
    def test_deve_retornar_1_tupla(self):
        self.assertEqual(filter_users(get_users()), [(140, 'Júlia', 'julia_sensacao@hotmail.com'), (235, 'Marina', 'marina_s2@hotmail.com'), (500, 'Bruna', 'bruna_costa@hotmail.com'), (507, 'Jorge', 'jorgin_gatin@hotmail.com')])
        

