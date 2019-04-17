class Lista(): 

    def __init__(self):
        self.lista = []

    def __add__(self, val):
        self.lista.append(val)
        return self.lista

l = Lista()

print(l+1)
print(l+2)
print(2+l)