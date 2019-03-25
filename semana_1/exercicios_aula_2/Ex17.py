'''
Problema #17
Faça uma função que receba uma função e uma lista de números, aplique essa
função a todos os valores da lista e retorne uma nova lista com os valores
processados:
EX:
aplica(func, list) -> [func(list[0]), func(list[n]), ..]
aplica(soma_1, [1, 2, 3]) -> [2, 3, 4]
aplica(sub_1, [1, 2, 3]) -> [0, 1, 2]
'''
lista = [1, 2, 3]

def sum(num): 
    return num + 1

def sub(num):
    return num - 1

def aplica(fun, list):
    novaLista = []
    for x in list:
        novaLista.append(fun(x))
    return novaLista

print(aplica(sum, [1, 2, 3]))
print(aplica(sub, [1, 2, 3]))

