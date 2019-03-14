'''
Exercício # 12
Faça um programa que receba uma string, com um número de ponto flutuante, e
imprima qual a parte dele que não é inteira
EX:
n = ‘3.14’
responsta: 14
'''

valor = str(input("Informe um número real: "))

final = valor.split('.')[1]

print(final)



