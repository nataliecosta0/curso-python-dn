'''
Problema #16
Faça uma função que receba uma função e um número. Ela deve retornar uma
lista com todos os números em ordem crescente até aquele valor:
EX:
aplica_em_lote(soma_1, 3) -> [1, 2, 3]
DICA:
O index inicia em 0
'''
def soma_1(numeros):
    return numeros +1

def aplicacao_em_lote(val, numeros):
    lista = []
    for elemento in range(numeros):
        lista.append(val(elemento))
    return lista

print(aplicacao_em_lote(soma_1, 9))
