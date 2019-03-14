'''
Exercício #7
Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim, quais são? E também diga se ela é uma frase ou não.
'''

valor = str(input("Informe qualquer valor: "))

if 'a' or 'e' or 'i' or 'o' or 'u' in valor:
    print("Tem vogal")

if valor.find(' '):
    print("É frase")
else:
    print("Não é frase")

