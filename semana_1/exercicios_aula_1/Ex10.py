'''
Exercício #10
Faça um programa que leia 5 números e informe o maior número.
'''

quantidade = 0
maior = 0

while quantidade < 5:
    quantidade = quantidade + 1
    numero = int(input("Informe um número: "))
    if numero > maior:
        maior = numero

print(f'O maior número é {maior}')