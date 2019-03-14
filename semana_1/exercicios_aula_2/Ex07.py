'''
Problema #7
Faça um programa que faça a inversão de uma lista usando as propriedade
mutáveis dessa lista (remova da lista e insira de novo)
Ex:
Entrada = [1, 2, 3]
Saída = [3, 2, 1]
Coisas que podem te ajudar:
list.insert, list.append, list.remove
'''

listaEntrada = [1, 2, 3]
listaSaida = []

for i in listaEntrada:
    listaSaida.insert(0, i)

print(listaSaida)