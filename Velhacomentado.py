# ============================================
# CP02 – JOGO DA VELHA (Matriz 3x3)
# Disciplina: Programação em Python – FIAP
# Aluno: Roberto Batista de Oliveira
# Data: 19/10/2023
# ============================================

# 🧱 BLOCO 1 – Função para exibir o tabuleiro
# Mostra a matriz 3x3 a cada jogada, com linhas e colunas separadas visualmente.
def exibir_tabuleiro(tabuleiro):
    print()
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print()

# 🧱 BLOCO 2 – Função para validar jogadas
# Garante que o número digitado está entre 1 e 9 e que a posição ainda está vazia.
def jogada_valida(tabuleiro, posicao):
    if not (1 <= posicao <= 9):
        return False
    lin = (posicao - 1) // 3
    col = (posicao - 1) % 3
    return tabuleiro[lin][col] == " "

# 🧱 BLOCO 3 – Função para verificar o vencedor
# Checa linhas, colunas e diagonais para ver se há três símbolos iguais.
def verificar_vencedor(tab):
    linhas = tab
    colunas = [[tab[0][c], tab[1][c], tab[2][c]] for c in range(3)]
    diagonais = [[tab[0][0], tab[1][1], tab[2][2]],
                 [tab[0][2], tab[1][1], tab[2][0]]]
    for trio in linhas + colunas + diagonais:
        if trio[0] != " " and trio.count(trio[0]) == 3:
            return trio[0]  # retorna "X" ou "O"
    return None

# 🧱 BLOCO 4 – Função para verificar empate
# Se o tabuleiro estiver cheio e não houver vencedor, o jogo empata.
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# 🧱 BLOCO 5 – Função principal do jogo
# Controla a lógica principal: alternância de jogadores, leitura de jogadas e fim do jogo.
def jogar():
    # cria uma matriz 3x3 vazia
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    print("🎮 JOGO DA VELHA – PvP (Jogador X vs Jogador O)")
    print("Use os números de 1 a 9 para escolher uma posição:\n")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    # Loop principal do jogo
    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            pos = int(input(f"👉 Jogador {jogador_atual}, escolha uma posição (1-9): "))
        except ValueError:
            print("⚠️ Digite um número válido entre 1 e 9.")
            continue

        # valida se a jogada é possível
        if not jogada_valida(tabuleiro, pos):
            print("❌ Posição inválida ou já ocupada. Tente novamente.")
            continue

        # converte número para coordenadas da matriz
        lin = (pos - 1) // 3
        col = (pos - 1) % 3
        tabuleiro[lin][col] = jogador_atual

        # verifica vitória
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"🏆 Jogador {vencedor} venceu!")
            break

        # verifica empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("🤝 Empate!")
            break

        # alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# 🧱 BLOCO 6 – Ponto de entrada do programa
# Garante que o jogo só é executado quando o arquivo for rodado diretamente.
if __name__ == "__main__":
    jogar()