'''
Exercício #4
Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
● O produto do dobro do primeiro com metade do segundo .
● A soma do triplo do primeiro com o terceiro.
● O terceiro elevado ao cubo.
'''

num1 = int(input("Informe um número inteiro: "))
num2 = int(input(("Informe outro número inteiro: ")))
num3 = float(input("Informe um número real: "))

calculoUm = float((num1*num1) * (num2/2))
calculoDois = float((num1*3) + num3)
calculoTres = float(num3**3)

print(f'Resultado 1: {calculoUm}\nResultado 2: {calculoDois}\nResultado 3: {calculoTres}')