# Como entrada, receba um número inteiro referente ao tamanho do jogo, defina um número aleatório referente ao tamanho do jogo, e depois solicite ao jogador um número para tentar adivinha-lo e siga tentando até adivinhar

import random
tamanho_jogo = int(input("Defina o tamanho do jogo (número máximo): "))
numero_aleatorio = random.randint(1, tamanho_jogo)
tentativa = None
while tentativa != numero_aleatorio:
    tentativa = int(input(f"Tente adivinhar o número entre 1 e {tamanho_jogo}: "))
    if tentativa < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número.")

# Fim do código

