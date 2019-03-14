'''
Problema #6
Usando os mesmos inputs do código anterior, reconstrua o problema de maneira
declarativa.
Funções que pode te ajudar:
- operator.mul
- map()
'''
listaEntrada = ['foo', 'bar', 'spam', 'eggs']
print(list(x + x for x in listaEntrada))

