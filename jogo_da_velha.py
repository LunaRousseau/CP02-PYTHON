# Jogo da Velha em Python


def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)

def jogada_valida(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == " "

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    print("=== JOGO DA VELHA ===")
    print("Jogadores: X e O")
    exibir_tabuleiro(tabuleiro)

    while True:
        print(f"Vez do jogador {jogador_atual}")
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Por favor, digite números válidos.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição inválida! Escolha valores entre 0 e 2.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Essa posição já está ocupada. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        exibir_tabuleiro(tabuleiro)

        if verificar_vencedor(tabuleiro, jogador_atual):
            print(f"🏆 Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            print("🤝 Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()
