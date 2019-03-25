'''
Faça um programa, com uma função, que calcula a mediana de uma lista.
Funções embutidas que podem te ajudar:
● sorted(lista) -> ordena a lista
'''
lista = [10, 1, 9, 5, 5]
'''
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
'''
def mediana(lista):
    tamanho = len(lista)
    lista_ordenada = sorted(lista)
    central = tamanho//2

    if tamanho % 2:
        return lista_ordenada[central]
    else:
        baixo = central - 1
        alto = central
        return (lista_ordenada[baixo] + lista_ordenada[alto]) / 2

print(f'Mediana: {mediana(lista)}')