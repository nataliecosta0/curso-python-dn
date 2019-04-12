'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class BichinhoVirtual():
    def __init__(self, nome = 'Recem', fome = 10, saude = 10, idade = 1):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self):
        novoNome = input("Informe um novo nome do seu bichado: ")
        self.nome = novoNome
        print("Nome: {}".format(self.nome))

    def fome_atual(self):
        nivelFome = int(input("Fome: "))
        self.fome = nivelFome
        
    def saude_atual(self):
        nivelSaude = int(input("Saúde: "))
        self.saude = nivelSaude

    def idade_atual(self):
        nivelIdade = int(input("Idade: "))
        self.idade = nivelIdade

    def mostrar(self):
        print("\nA fome atual do seu bichano é: {}".format(self.fome))
        print("\nA saúde atual do seu bichano é: {}".format(self.saude))
        print("\nA idade atual do seu bichano é: {}".format(self.idade))

    def humor(self):
        if self.fome < 5 or self.saude < 5:
            print("\nHumor baixo\n")
        elif (self.fome >= 5 and self.fome <= 7) or (self.saude >= 5 and self.saude <= 7):
            print("\nHumor médio\n")
        else:
            print("\nHumor alto\n")

b1 = BichinhoVirtual()
b1.alterarNome()
b1.fome_atual()
b1.saude_atual()
b1.idade_atual()
b1.mostrar()
b1.humor()