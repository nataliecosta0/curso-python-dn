'''
Exercício #9
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
'''

nota1 = int(input("Informe uma nota: "))

while nota1>=0 and nota1 <=10:
    print("Nota válida")
    nota1 = int(input("Informe uma nota: "))
else:
    print("Nota inválida")