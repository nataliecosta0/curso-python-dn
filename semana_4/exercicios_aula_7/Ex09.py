'''
Exercício #9
Cria uma função que lê um arquivo, caso ele não exista, não quebre a execução,
apenas responda que o arquivo não existe
'''

def leitura_arquivo(arquivo: str):
    try:
        return open(arquivo)
    except FileNotFoundError:
        return 'Arquivo não existe'

print(leitura_arquivo('textinho.txt'))