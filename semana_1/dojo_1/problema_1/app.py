'''
problema 1
Complete a solução para que ela inverta todas as palavras dentro da string passada.
Exemplo:
reverse_worlds("A maior vitória é aquela que não requer batalha")
# 'batalha requer não que aquela é vitória maior A'
'''

def reverse_worlds(frase):
    lista = frase.split(' ')
    return ' '.join(list(reversed(lista)))