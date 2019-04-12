'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class Tv():
    def ___init__(self, numero = 1, volume = 2):
        self.numero = numero
        self.volume = volume

    def numeroCanal(self):
        canal = int(input("Informe o número do canal: "))
        if canal > 0 and canal <= 60:
            self.numero = canal
            print("\nO número do canal é: {}".format(self.numero))
        else:
            print("\nCanal Inválido.")

    def mudarVolume(self):
        mudarVolumeA = int(input("\nInforme o aumento de volume: "))
        if mudarVolumeA > 0 and mudarVolumeA <= 100:
            self.volume = mudarVolumeA
            print("\nO volume após o aumento é: {}".format(self.volume))
        else:
            print("\nVolume inválido.")

t = Tv()
t.numeroCanal()
t.mudarVolume()