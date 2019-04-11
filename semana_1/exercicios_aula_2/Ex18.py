'''
Problema #18
Usando as funções criadas nos exercícios 13, 14 e 15.
Crie uma composição de funções que resolva os 3 casos:
EX:
f(x) -> Union[ID, goiabada, queijo, romeu e julieta]
f(3) -> ‘queijo’
f(5) -> ‘goiabada’
f(15) -> ‘romeu e julieta’
f(19) -> 19
'''

numero = int(input("Informe um número: "))

def resulQueijo(numero):
    if numero % 3 == 0:
        return 'queijo'
    else:
        return numero

def resulGoiabada(numero):
    if numero % 5 == 0:
        return 'goiabada'
    else:
        return numero

def resulRomeuJulieta(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'romeu e julieta'
    else:
        return numero

