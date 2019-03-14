'''
Exercício # 11
Faça um programa que itere em uma string e toda vez que uma vogal aparecer
na sua string print o seu nome entre as letras
string = bananas
b
eduardo
n
eduardo
n
'''

nome = str(input("Informe seu nome: "))
palavra = str(input("Informe uma palavra: "))

for vogal in palavra:
    if vogal in 'aeiou':
        print(nome)
    else:
        print(vogal)
