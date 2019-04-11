'''
Classe Pessoa: Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5 # se a idade for menor que 21, irá acrescer 0.5 na altura (já definida)

        self.idade += 1 # o metodo vai envelhecer 1 ano 

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')


nat = Pessoa('Natalie', 19, 54, 163)
nat.mostraPessoa()
nat.envelhecer()
nat.emagrecer(3)
nat.mostraPessoa()
