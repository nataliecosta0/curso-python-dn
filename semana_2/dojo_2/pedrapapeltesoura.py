'''
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

    Pedra empata com Pedra e ganha de Tesoura
    Tesoura empata com Tesoura e ganha de Papel
    Papel empata com Papel e ganha de Pedra
'''

from unittest import TestCase

def jogadas(escolher_jogada1, escolher_jogada2):
    dicionario = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura':'pedra'}

    if escolher_jogada1 == escolher_jogada2:
        return 'empatou!'

    if dicionario[escolher_jogada1] == escolher_jogada2:
        return escolher_jogada2 + ' ganhou!'
    
    else:
        return escolher_jogada1 + ' ganhou!'

    if escolher_jogada1 not in ['pedra', 'papel', 'tesoura'] or escolher_jogada2 not in ['pedra', 'papel', 'tesoura']:
        return 'Valor inválido'

class Test_jokenpo(TestCase):

    #Empates
    def teste_pedra_com_pedra_deve_retornar_empate(self):
        self.assertEqual(jogadas('pedra', 'pedra'), 'empatou!')

    def teste_papel_com_papel_deve_retornar_empate(self):
        self.assertEqual(jogadas('papel', 'papel'), 'empatou!')

    def teste_tesoura_com_tesoura_deve_retornar_empate(self):
        self.assertEqual(jogadas('tesoura', 'tesoura'), 'empatou!')

    def teste_pedra_com_papel_deve_retornar_papel(self):
        self.assertEqual(jogadas('pedra', 'papel'), 'papel ganhou!')

    def teste_pedra_com_tesoura_deve_retornar_papel(self):
        self.assertEqual(jogadas('pedra', 'tesoura'), 'pedra ganhou!')

    def teste_papel_com_tesoura_deve_retornar_tesoura(self):
        self.assertEqual(jogadas('papel', 'tesoura'), 'tesoura ganhou!')

    def teste_papel_com_pedra_deve_retornar_papel(self):
        self.assertEqual(jogadas('papel', 'pedra'), 'papel ganhou!')

    def teste_tesoura_com_pedra_deve_retornar_pedra(self):
        self.assertEqual(jogadas('tesoura', 'pedra'), 'pedra ganhou!')

    def teste_tesoura_com_papel_deve_retornar_tesoura(self):
        self.assertEqual(jogadas('tesoura', 'papel'), 'tesoura ganhou!')

    