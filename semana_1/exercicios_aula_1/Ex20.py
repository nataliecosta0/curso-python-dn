'''
Baseando-se nos exercícios passados, monte um dicionário com os seguintes
seguintes chaves:
lista, somatório, tamanho, maior valor e menor valor
'''

lista = [1, 5, 8, 6, 8]
dicionario = {}

def dicionario(list):
    soma = sum(lista)
    tamanho = len(lista)
    maior = max(lista)
    menor = min(lista)
    return (f'A soma é: {soma}, o tamanho é {tamanho}, o maior número é {maior} e o menor número é {menor}')

print(dicionario(lista))

