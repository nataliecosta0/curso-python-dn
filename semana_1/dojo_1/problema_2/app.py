'''
problema 2
Crie uma função is_divisible(n, x, y) que verifica se um número n é divisível por dois números x e y.
Todas as entradas são dígitos positivos, diferentes de zero.
Exemplos:
is_divisible(3,1,3)--> True
is_divisible(12,2,6)--> True
is_divisible(100,5,3)--> False
is_divisible(12,7,5)--> False
'''

def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False