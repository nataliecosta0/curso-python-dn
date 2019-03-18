'''
Problema #3
Dado o código:
Faça assertivas em relação ao que funciona e
não funciona nos seus casos de teste
'''

class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x + y
    
    def mult(self, x, y):
        return x + y

    def div(self, x, y):
        return x * y

c = Calc()

assert c.add(1, 1) == 2
assert c.sub(1, 1) == 0
assert c.mult(1, 1) == 1
assert c.div(1, 1) == 1