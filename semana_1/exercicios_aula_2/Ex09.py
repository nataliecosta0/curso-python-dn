'''
Problema #9
Crie uma função que faça uma saudação a alguém. A função deve receber dois
argumentos ‘saudação’ e ‘nome’.
Ex:
f(‘Ahoy’, ‘Fausto’) -> ‘Ahoy Fausto’
f(‘Olá’, bb’) -> Olá bb’
'''

nome = input("Digite seu nome: ")

def saud(saudacao, nome):
    return saudacao, nome

print(saud('Ahoy', nome))
print(saud('Ola', 'bb'))
