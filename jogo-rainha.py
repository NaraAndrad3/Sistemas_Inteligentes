def verifica_ataque(rainhas):
    for i in range(len(rainhas)):
        for j in range(i + 1, len(rainhas)):
            x1, y1 = rainhas[i]
            x2, y2 = rainhas[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return True
    return False

def dfs(linha, rainhas):
    if linha == 8:
        return [rainhas.copy()]

    solutions = []
    for coluna in range(8):
        rainha = (linha, coluna)
        rainhas.append(rainha)
        if not verifica_ataque(rainhas):
            for child in dfs(linha + 1, rainhas):
                solutions.append(child)
        rainhas.pop()

    return solutions

def mostra_tabuleiro(rainhas):
    tabuleiro = [['.' for _ in range(8)] for _ in range(8)]
    for rainha in rainhas:
        tabuleiro[rainha[0]][rainha[1]] = 'X'
    for linha in tabuleiro:
        print(' '.join(linha))

def main():
    rainhas = []
    solutions = dfs(0, rainhas)

    for i, sol in enumerate(solutions):
        print(f'Solução {i + 1}:')
        mostra_tabuleiro(sol)
        print()

main()