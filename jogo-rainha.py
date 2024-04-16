def dfs(linha, rainhas, size):
    if linha == size:
        return [rainhas.copy()]

    solutions = []
    for coluna in range(size):
        rainha = (linha, coluna)
        if not tem_ataque(rainhas, rainha):  
            rainhas.append(rainha)
            for child in dfs(linha + 1, rainhas, size): 
                solutions.append(child)
            rainhas.pop()

    return solutions

def tem_ataque(rainhas, nova_rainha):
    for rainha in rainhas:
        if rainha[0] == nova_rainha[0] or rainha[1] == nova_rainha[1] or abs(rainha[0] - nova_rainha[0]) == abs(rainha[1] - nova_rainha[1]):
            return True
    return False

def mostra_tabuleiro(rainhas, size):
    for i in range(size):
        linha = ''
        for j in range(size):
            if (i, j) in rainhas:
                linha += 'X '
            else:
                linha += '. '
        print(linha)


def main():
    size = 12;
    rainhas = []
    solutions = dfs(0, rainhas, size)

    for i, sol in enumerate(solutions):
        print(f'Solução {i + 1}:')
        mostra_tabuleiro(sol, size)
        print()

main()