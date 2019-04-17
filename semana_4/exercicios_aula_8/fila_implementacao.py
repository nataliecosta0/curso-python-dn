
class Fila(): 
    #fila = 0
    def __init__(self):
        self.fila = []

    def __str__(self):
        return f'{self.fila}' 

    def inserir(self, val):
        return self.fila.append(val)

    def deletar(self):
        return self.fila.pop(0)

f = Fila()

print(f)

f.inserir(5)
f.inserir(6)
f.inserir(7)
f.inserir(8)
f.inserir(9)

print(f)

print(f.deletar())

print(f)


