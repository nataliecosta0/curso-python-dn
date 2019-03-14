"""
Exercício #8
Faça um programa que receba uma data de nascimento (15/07/87) e imprima
‘Você nasceu em <dia> de <mes> de <ano>
"""

data_nascimento = input("Informe a data de nascimento: ")

dia, mes, ano = data_nascimento.split('/')

print(f'Você nascem em {dia} de {mes} de {ano}')