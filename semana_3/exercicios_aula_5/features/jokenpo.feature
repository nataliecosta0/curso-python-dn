# language:pt

Funcionalidade: Jokenpo
  Dados 2 capitães de times de futebol
  Eles devem jogar jokenpo
  Para decidir quem escolherá o primeiro jogador

Cenário: Capt. A e Capt. B empatams
  Quando C.A jogar "papel" e C.B jogar "papel"
  Então gera empate

Cenário: Capt. A ganha Capt. B
  Quando C.A jogar "Papel" e C.B jogar "Pedra"
  Então "Papel" ganha
