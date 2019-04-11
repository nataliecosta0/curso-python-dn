'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        print(self.numero_conta, self.nome_correntista, self.saldo)

    def alterarNome(self, nome):
        self.nome_correntista =  nome
        print(nome)

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print(self.saldo)

    def saque(self, valor):
        self.saldo = self.saldo - valor
        print(self.saldo)

t = ContaCorrente(123, 'Natalie', 200)
t.alterarNome('Júlia')
t.deposito(200)
t.saque(20)
