'''
Problema #7
Revisite os testes do problema 6 e os renomeie baseado em critérios de aceite.
'''

from unittest import TestCase

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

class Test_funcao_filtrar(TestCase):
    def test_deve_retornar_usuarios_tupla_com_id_maior_que_100(self):
        self.assertEqual(filter_users(get_users()), [(140, 'Júlia', 'julia_sensacao@hotmail.com'), (235, 'Marina', 'marina_s2@hotmail.com'), (500, 'Bruna', 'bruna_costa@hotmail.com'), (507, 'Jorge', 'jorgin_gatin@hotmail.com')])