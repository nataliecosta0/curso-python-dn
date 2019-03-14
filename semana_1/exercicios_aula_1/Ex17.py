'''
Faça um programa, com uma função, que calcula a mediana de uma lista.
Funções embutidas que podem te ajudar:
● sorted(lista) -> ordena a lista
'''

lista = [10, 1, 9, 5]

def ordem(lista):
    listaOrdem = sorted(lista)
    tamanho = len(listaOrdem)
    mediana = tamanho//2

    if tamanho % 2 == 0:
        return listaOrdem[mediana]
    else:
        anterior = mediana -1
        posterior = mediana
        return (listaOrdem [anterior] + listaOrdem[posterior]) / 2 

print(f'Mediana: {ordem(lista)}')