'''
Problema #10
Especifique uma função que receba um número uma string e retorne se na string
há o mesmo número de elementos que foram passados no parâmetro
Ex:
f(3, ‘aaa’) -> True
f(10, ‘Batata’) -> False
'''

numero = int(input("Informe um número: "))
palavra = str(input("Informe uma palavra: "))

def igual(numero, palavra):
    comparacao = len(palavra)
    if comparacao == numero:
        return True
    else:
        return False

print(igual(numero, palavra))