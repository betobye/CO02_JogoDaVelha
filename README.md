CP02 – Jogo da Velha em Python
FIAP – 1TIA-PR | Disciplina: Computational Thinking with Python*

---

Aluno
- Roberto Batista de Oliveira - RM 567239

---

Descrição
Este projeto implementa o Jogo da Velha em Python, utilizando uma *matriz 3x3* para representar o tabuleiro e alternância entre dois jogadores (X e O).

O jogo exibe o tabuleiro a cada jogada, valida as jogadas, verifica vitórias ou empate e alterna automaticamente o jogador ativo.

---

Funcionalidades
- Exibe o tabuleiro após cada jogada  
- Impede jogadas em posições já ocupadas  
- Verifica vitória em linhas, colunas e diagonais  
- Detecta empate automaticamente  
- Alterna entre os jogadores X e O  

---

Estrutura do Código
- exibir_tabuleiro() → Mostra o estado atual do jogo  
- verificar_vencedor() → Verifica se há um ganhador  
- verificar_empate() → Determina se houve empate  
- jogada_valida() → Impede jogadas inválidas  
- jogar() → Controla o loop principal do jogo  

---

Como Executar
1. Certifique-se de ter o *Python 3* instalado.  
2. Clone ou baixe este repositório:  
   ```bash
   git clone https://github.com/betobye/CO02_JogoDaVelha.git
   cd CO02_JogoDaVelha
