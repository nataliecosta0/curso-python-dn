'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado():

    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self):
        self.tamanho_lado = 5

    def retornar_valor_lado(self):
        print('O valor do lado é {}'.format(self.tamanho_lado))

    def calcular_area(self):
        print('O valor da area é {}'.format(self.tamanho_lado**2))

q1 = Quadrado(2)
q1.calcular_area()
q1.mudar_valor_lado()
q1.retornar_valor_lado()
q1.calcular_area()
