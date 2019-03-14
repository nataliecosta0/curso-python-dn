'''
Exercício #18
Faça um programa, com uma função que dado uma lista e uma posição da
mesma faça o quartil dessa posição.
p_index = int(p * len(lista))
'''

lista = [1, 2, 3, 5, 4]


def quantil(lista, p):
    posicao = int(p * (len(lista)))
    ordem = sorted(lista)[posicao]
    return ordem

print(quantil(lista, 0.90))