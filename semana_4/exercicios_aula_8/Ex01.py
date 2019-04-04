'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola():

    def __init__(self, cor, circunferencia, material):
        self.cor = cor 
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = 'verde'

    def mostraCor(self):
        print('A cor da bola é {}'.format(self.cor))


b1 = Bola('amarela', 3.14, 'plastico')

b1.mostraCor()
b1.trocaCor()
b1.mostraCor()

