'''
Problema #12
Faça uma função que receba um número, caso esse número seja múltiplo de 3,
retorne “queijo”, caso contrário, retorne o valor de entrada.
EX:
f(5) -> 5
f(3) -> ‘queijo’
f(6) -> ‘queijo’
...
'''

numero = int(input("Informe um número: "))

def resulQueijo(numero):
    if numero % 3 == 0:
        return 'queijo'
    else:
        return numero

print(resulQueijo(numero))