'''
problema 3
Pegue duas strings s1 e s2 e com elas monte uma nova string contendo todos os caracteres das duas strings.
Regras:

Não deve haver chars repetidos
Eles devem estar em ordem alfabética
'''
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))