'''
19. Dada uma lista:

[‘keep’, ‘remove’, ‘keep’, ‘remove’, ‘keep’, ‘remove’]
Usando a função filter remova tudo que deve ser removido
'''

lista = ['keep', 'remove', 'keep', 'remove', 'keep']
nova_lista = list(filter(lambda x: x != 'remove', lista))

print(nova_lista)
