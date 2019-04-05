'''
Exercício #8
Faça uma função chamada ‘get_html’ que tem como parâmetro uma url.
A função deve fazer uma chamada a url desejada e salvar seu código html em um
arquivo.
'''
import urllib.request

def get_html():
    chamada = urllib.request.urlopen("http://google.com")
    return chamada.read().decode('latin-1')

#print(get_html())
    
with open('arquivo_para_html.txt', 'w') as arquivo:
    arquivo.writelines(get_html())
