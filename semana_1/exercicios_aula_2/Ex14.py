'''
Problema #14
Faça uma função que receba um número, caso esse número seja múltiplo de 3 e
5, retorne “romeu e julieta”, caso contrário, retorne o valor de entrada.
EX:
f(3) -> 3
f(5) -> 5
f(15) -> ‘romeu e juleita’
...
'''

numero = int(input("Informe um número: "))

def resulRomeuJulieta(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'romeu e julieta'
    else:
        return numero

print(resulRomeuJulieta(numero))