'''
Problema #21
Dada uma lista:
[‘keep’, ‘remove’, ‘keep’, ‘remove’, ‘keep’, ‘remove’]
Usando a função reduce faça a somatória de todos os elementos da lista juntos
EX:
[‘a’, ‘abc’, ‘def’] -> 7
'''
from functools import reduce

lista = ['keep', 'remove', 'keep', 'remove', 'keep']
resultadoSoma = reduce(lambda x, y: x + y, ['keep', 'remove', 'keep', 'remove', 'keep'])

print(len(resultadoSoma))




