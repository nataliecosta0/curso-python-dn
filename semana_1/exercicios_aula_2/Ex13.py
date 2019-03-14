'''
Problema #13
Faça uma função que receba um número, caso esse número seja múltiplo de 5,
retorne “goiabada”, caso contrário, retorne o valor de entrada.
EX:
f(5) -> ‘goiabada’
f(3) -> 3
f(10) -> ‘goiabada’
...
'''

numero = int(input("Informe um número: "))

def resulGoiabada(numero):
    if numero % 5 == 0:
        return 'goiabada'
    else:
        return numero

print(resulGoiabada(numero))