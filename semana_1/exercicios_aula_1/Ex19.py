'''
Faça um programa, com uma função, que calcule a dispersão de uma lista
Funções embutidas que podem te ajudar:
● min(lista) -> retorna o menor valor
● max(lista) -> retorna o maior valor
'''

lista = [5, 8, 9, 10, 1]

def dispersao(list):
    menor = min(lista)
    maior = max(lista)

    return (maior - menor)

print(dispersao(lista))