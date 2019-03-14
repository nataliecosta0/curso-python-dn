'''
Exercício #21
Dada uma lista de entradas de usuário de números inteiros, construa um
dicionário com a lista padrão, a lista dos valores elevados ao quadrado e a lista
dos valores elevados ao cubo
'''
lista = []
dicionario = {}
#i = 0

decisao = str(input("Deseja inserir um número na lista? [S/N]")).upper()

while decisao == 'S':
    lista.append(int(input("Informe um número inteiro: ")))
    decisao = str(input("Deseja inserir mais um número? [S/N]")).upper()
else:
    print("Fim da lista: ")

def quadrado(lista):
    return [i**2 for i in lista]

def cubo(lista):
    return[i**3 for i in lista]

dicionario['lista original'] = lista
dicionario['lista ao quadrado'] = quadrado(lista)
dicionario['lista ao cubo'] = cubo(lista)

print(dicionario)


