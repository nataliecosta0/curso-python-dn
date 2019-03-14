lista = ['keep', 'remove', 'keep', 'remove', 'keep']
nova_lista = list(filter(lambda x: x != 'remove', lista))

print(nova_lista)
