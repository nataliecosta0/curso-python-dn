'''
Problema #15
Faça uma função que se aplique uma função duas vezes em um valor passado
EX:
reaplica(soma_2, 2) -> 6
reaplica(sub_2, 2) -> -2
'''

def soma_2(x):
    return x + 2

def sub_2(x):
    return x - 2

def aplicacao(val, x):
    return val(val(x))

print(aplicacao(soma_2, 2))
print(aplicacao(sub_2,2))
