'''
Exercício #6
Leia o arquivo criado no exercício 5 e transforme cada linha do arquivo em um
elemento de uma lista
[‘1 x 10 = 10’, (...), ‘10 x 10 = 100’]
'''

arquivo = open('alteracao_texto.txt', 'w')

tabuada = [f'{x} x 10 = {x * 10}\n' for x in range(1, 11)]

tabuada.split()

arquivo.writelines(list(tabuada)