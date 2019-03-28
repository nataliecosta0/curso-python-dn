from behave import when, then
from typing import Text 

def jogo_jokenpo(mao_jogador1: Text, mao_jogador2: Text) -> Text:
    '''
    Jogo do jokenpo

    Regras de entrada: Cada jogador escolhe um elemento valido(pedra, tesoura, papel). O resultado será
    avaliado com base em regras pré-definidas:
        - Pedra ganha de tesoura;
        - Tesoura ganha de Papel;
        - Papel ganha de pedra;
        - Entradas iguais empata.
    Caso o elemento não esteja dentro da lista, retorna invalido.

    >>> jogo_jokenpo('tesoura', 'tesoura')
    'Empate'

    >>> jogo_jokenpo('vassoura', 'papel')
    'Argumento inválido'

    >>> jogo_jokenpo('Pedra', 'tesoura')
    'Pedra Ganhou'

    '''
    dicionario = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura': 'pedra'}

    mao_jogador1 = mao_jogador1.lower()
    mao_jogador2 = mao_jogador2.lower()

    if mao_jogador1 not in [
        "pedra",
        "papel",
        "tesoura",
    ] or mao_jogador2 not in ["pedra", "papel", "tesoura"]:

        return "Argumento inválido"

    if mao_jogador1 == mao_jogador2:
        return "Empate"

    if dicionario[mao_jogador1] == mao_jogador2:
        return mao_jogador2.capitalize() + " Ganhou!"
    else:
        return mao_jogador1.capitalize() + " Ganhou!"


@when('C.A jogar "{mao_1}" e C.B jogar "{mao_2}"')
def jogada_igual(c, mao_1, mao_2):
    c.resultado_jogada = jogo_jokenpo(mao_1, mao_2)


@then('gera empate')
def assertiva_jogada_igual(c):
    assert c.resultado_jogada == 'Empate'


@then('"{jogada}" ganha')
def assertiva_jogada_vencedora(c, jogada):
    assert c.resultado_jogada == f"{jogada} Ganhou!"

