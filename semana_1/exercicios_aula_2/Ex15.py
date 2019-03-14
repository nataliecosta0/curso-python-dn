'''
Problema #15
Faça uma função que se aplique uma função duas vezes em um valor passado
EX:
reaplica(soma_2, 2) -> 6
reaplica(sub_2, 2) -> -2
'''

def soma_2(n):
    return n + 2

def sub(x, y):
    return x - y

def aplicacao(op, val):
    return op(op(val))


