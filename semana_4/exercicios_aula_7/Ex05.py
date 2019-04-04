'''
Exercício #5
Crie um arquivo de texto usando a função open com a tabuada do 10.
1 x 10 = 10
(...)
10 x 10 = 100
'''
#arquivo = open('alteracao_texto.txt', 'r')

tabuada = []

tabuada = [f'{x} x 10 = {x * 10}\n' for x in range(1, 11)]

tabuada.split(' ')

#arquivo.writelines(tabuada)

print(tabuada)
