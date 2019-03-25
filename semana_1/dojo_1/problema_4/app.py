'''
problema 4
Dado um dicionário de linguagens e seus respectivos resultados de teste, retorne a lista das linguagens onde sua pontuação
de teste é pelo menos 60, em ordem decrescente dos resultados.
Nota: Não haverá valores duplicados.
{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> []
'''

def my_languages(dicionario):
    return [key for key, value in dicionario.items() if value >= 60]
  