'''
Problema #8
Resolva de maneira imutável (Ou seja, retornando uma nova lista)
Ex:
Entrada = [1, 2, 3]
Saída = [3, 2, 1]
Coisas que podem te ajudar:
list.insert, list.append, list.remove

'''
listaEntrada = [1, 2, 3]
listaSaida = []

listaSaida = list(reversed(listaEntrada))

print(listaSaida)