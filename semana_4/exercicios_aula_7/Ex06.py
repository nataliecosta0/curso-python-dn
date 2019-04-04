'''
Exercício #6
Leia o arquivo criado no exercício 5 e transforme cada linha do arquivo em um
elemento de uma lista
[‘1 x 10 = 10’, (...), ‘10 x 10 = 100’]
'''

arquivo = open('alteracao_texto.txt', 'r')
print(arquivo.readlines())