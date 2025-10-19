# ==========================================
# JOGO DA VELHA EM PYTHON (com MATRIZ 3x3)
# ==========================================
# CP01 - Aula 03 (FIAP)
# Aluno: Roberto Batista de Oliveira
# Data: 19/10/2023
# ==========================================

# -------------------------------
# 1️⃣ Função para exibir o tabuleiro
# -------------------------------
def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print("\n")

# -------------------------------
# 2️⃣ Função para verificar vencedor
# -------------------------------
def verificar_vencedor(tabuleiro):
    # Linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    # Colunas
    for c in range(3):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] != " ":
            return tabuleiro[0][c]

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None  # ainda não há vencedor

# -------------------------------
# 3️⃣ Função para verificar empate
# -------------------------------
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False  # ainda há espaços
    return True  # todas as células preenchidas

# -------------------------------
# 4️⃣ Função para validar jogada
# -------------------------------
def jogada_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    if tabuleiro[linha][coluna] != " ":
        return False
    return True

# -------------------------------
# 5️⃣ Loop principal do jogo
# -------------------------------
def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Digite apenas números válidos (0, 1 ou 2).")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida! Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# -------------------------------
# Ponto de entrada
# -------------------------------
if __name__ == "_main_":
    jogar()