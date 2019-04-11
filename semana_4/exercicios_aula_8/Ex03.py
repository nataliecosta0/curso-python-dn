'''
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de 
um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo():
    
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor_lados(self):
        self.ladoA = 5
        self.ladoB = 2

    def retornar_valor_lados(self):
        print("\nO valor do lado A é {} e o valor do lado B é {}".format(self.ladoA, self.ladoB))

    def calcularArea(self):
        print('\n O valor da area é {}'.format(self.ladoA * self.ladoB))

    def calcularPerímetro(self):
        print('\n O valor do perímetro é {}'.format((self.ladoA * 2) + (self.ladoB * 2)))
    
r1 = Retangulo(10, 15)
r1.calcularArea()
r1.calcularPerímetro()
print('---------------------------------')
r1.mudar_valor_lados()
r1.calcularArea()
r1.calcularPerímetro()



