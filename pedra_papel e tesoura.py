def jogar_pedra_papel_tesoura(jogada_usuario1, jogada_usuario2):
    opcoes = ['pedra', 'papel', 'tesoura']
    
    if jogada_usuario1 not in opcoes or jogada_usuario2 not in opcoes:
        return "Jogada inválida. Escolha entre 'pedra', 'papel' ou 'tesoura'."
    
    resultado = {
        'pedra': {'pedra': 'Empate', 'papel': 'Jogador 2 venceu', 'tesoura': 'Jogador 1 venceu'},
        'papel': {'pedra': 'Jogador 1 venceu', 'papel': 'Empate', 'tesoura': 'Jogador 2 venceu'},
        'tesoura': {'pedra': 'Jogador 2 venceu', 'papel': 'Jogador 1 venceu', 'tesoura': 'Empate'}
    }
    
    mensagem = f"Jogador 1 escolheu: {jogada_usuario1}\nJogador 2 escolheu: {jogada_usuario2}\n"
    mensagem += f"Resultado: {resultado[jogada_usuario1][jogada_usuario2]}"
    
    return mensagem

if __name__ == "__main__":
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
    while True:
        jogada_jogador1 = input("Jogador 1, digite sua jogada (pedra, papel ou tesoura) ou 'sair' para encerrar o jogo: ").lower()
        
        if jogada_jogador1 == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break
        
        jogada_jogador2 = input("Jogador 2, digite sua jogada (pedra, papel ou tesoura) ou 'sair' para encerrar o jogo: ").lower()
        
        if jogada_jogador2 == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break
        
        resultado = jogar_pedra_papel_tesoura(jogada_jogador1, jogada_jogador2)
        print(resultado)
