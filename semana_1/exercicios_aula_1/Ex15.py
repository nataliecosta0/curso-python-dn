'''
Exercício #15
Faça um programa que dada a entrada de uma lista ele calcule as combinações e
nos retorne as combinações em uma nova lista.
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saida: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
'''

listaEntrada = [1, 2, 3, 4]

for inicio in listaEntrada:
    for inicio_novo in listaEntrada:
        print([inicio, inicio_novo])