'''
Exercício #13
Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número
inteiro, imprima a tabuada desse número.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Informe um número para imprimir a tabuada: "))

for multiplicador in lista:
    resultado = multiplicador * num
    print(f'{multiplicador} * {num} = {resultado}')