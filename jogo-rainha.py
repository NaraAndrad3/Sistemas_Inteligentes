def verifica_ataque(solucao):
    for i in range(1, len(solucao)):
        for j in range(0, i):
            a, b = solucao[i]
            c, d = solucao[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return True
    return False

def dfs(size):
    pilha = [[]]  # armazena a organização das rainhas
    solucoes = []

    if size < 1:
        return []

    while pilha:
        sol = pilha.pop()
        row = len(sol)

        if row == size:
            if not verifica_ataque(sol):
                solucoes.append(sol)
            continue

        if row < size:
            for col in range(size):
                queen = (row, col) # cria uma rainha
                queens = sol.copy()
                queens.append(queen)
                pilha.append(queens)

    return solucoes

def mostra_tabuleiro(size, solucoes):
    for i in range(size):
        #print(' ---' * size)
        for j in range(size):
            p = 'X' if (i, j) in solucoes else '*'
            print('| %s ' % p, end='')
        print('|')
    #print(' --- ' * size)
    print('\n')

def main():
    size = 8
    row = 0
    solutions = dfs(size)

    for i, sol in enumerate(solutions):
        mostra_tabuleiro(size,sol)

main()