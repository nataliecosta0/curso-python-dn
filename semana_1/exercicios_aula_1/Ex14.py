'''
Exercício #14
Faça uma programa que dada a entrada de uma lista ele faça o calculo
acumulativo da mesma:
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [1, 3, 6, 10]
'''

listaEntrada = [1, 2, 3, 4]
listaSaida = []


for inicio, numero in enumerate(listaEntrada):
    listaSaida.append(sum(listaEntrada[:inicio+1]))

print(listaSaida)