'''
Problema #20
Dada uma lista:
[‘keep’, ‘remove’, ‘keep’, ‘remove’, ‘keep’, ‘remove’]
Usando a função map transforme o primeiro carácter em maiúsculo.
'''

lista = ['keep', 'remove', 'keep', 'remove', 'keep']
nova_lista = (list(map(lambda x: x.capitalize(), lista)))

print(nova_lista)