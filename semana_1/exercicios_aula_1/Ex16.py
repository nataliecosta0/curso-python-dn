'''
Exercício #16
Faça um programa, com uma função, que calcula a média de uma lista.
Funções embutidas que podem te ajudar:
● len(lista) -> calcula o tamanho da lista
● sum(lista) -> faz o somatório dos valores
'''

listaEntrada = [1, 2, 3, 4]

def media(listaEntrada):
    return (sum(listaEntrada)/len(listaEntrada))

print(f'A média da lista é: {media(listaEntrada)}')