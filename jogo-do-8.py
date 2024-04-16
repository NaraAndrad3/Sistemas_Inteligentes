from collections import deque
import random

def encontrar_posicao_vazia(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return i, j

def gerar_tabuleiro_inicial():
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for _ in range(1000):
        movimentos = []
        linha_vazia, coluna_vazia = encontrar_posicao_vazia(tabuleiro)

        if linha_vazia > 0:
            movimentos.append('cima')
        if linha_vazia < 2:
            movimentos.append('baixo')
        if coluna_vazia > 0:
            movimentos.append('esquerda')
        if coluna_vazia < 2:
            movimentos.append('direita')

        if movimentos:
            movimento = random.choice(movimentos)
            tabuleiro = aplicar_movimento(tabuleiro, movimento)
    return tabuleiro

def movimentos_possiveis(tabuleiro):
    movimentos = []
    linha_vazia, coluna_vazia = encontrar_posicao_vazia(tabuleiro)
    if linha_vazia > 0:
        movimentos.append('cima')
    if linha_vazia < 2:
        movimentos.append('baixo')
    if coluna_vazia > 0:
        movimentos.append('esquerda')
    if coluna_vazia < 2:
        movimentos.append('direita')
    return movimentos

def aplicar_movimento(tabuleiro, movimento):
    linha_vazia, coluna_vazia = encontrar_posicao_vazia(tabuleiro)
    novo_tabuleiro = [linha.copy() for linha in tabuleiro]

    if movimento == 'cima' and linha_vazia > 0:
        novo_tabuleiro[linha_vazia][coluna_vazia], novo_tabuleiro[linha_vazia - 1][coluna_vazia] = \
            novo_tabuleiro[linha_vazia - 1][coluna_vazia], novo_tabuleiro[linha_vazia][coluna_vazia]
    elif movimento == 'baixo' and linha_vazia < 2:
        novo_tabuleiro[linha_vazia][coluna_vazia], novo_tabuleiro[linha_vazia + 1][coluna_vazia] = \
            novo_tabuleiro[linha_vazia + 1][coluna_vazia], novo_tabuleiro[linha_vazia][coluna_vazia]
    elif movimento == 'esquerda' and coluna_vazia > 0:
        novo_tabuleiro[linha_vazia][coluna_vazia], novo_tabuleiro[linha_vazia][coluna_vazia - 1] = \
            novo_tabuleiro[linha_vazia][coluna_vazia - 1], novo_tabuleiro[linha_vazia][coluna_vazia]
    elif movimento == 'direita' and coluna_vazia < 2:
        novo_tabuleiro[linha_vazia][coluna_vazia], novo_tabuleiro[linha_vazia][coluna_vazia + 1] = \
            novo_tabuleiro[linha_vazia][coluna_vazia + 1], novo_tabuleiro[linha_vazia][coluna_vazia]
    return novo_tabuleiro

def resolver_jogo_do_8(tabuleiro_inicial, tabuleiro_meta):
    visitados = set()
    fila = deque([(tabuleiro_inicial, [])])
    while fila:
        tabuleiro, caminho = fila.popleft()
        if tabuleiro == tabuleiro_meta:
            return caminho
        tabuleiro_tupla = tuple(map(tuple, tabuleiro))
        if tabuleiro_tupla not in visitados:
            visitados.add(tabuleiro_tupla)
            for movimento in movimentos_possiveis(tabuleiro):
                novo_tabuleiro = aplicar_movimento(tabuleiro, movimento)
                fila.append((novo_tabuleiro, caminho + [movimento]))
    return None

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) if num != 0 else "_" for num in linha))
    print()

def main():
    tabuleiro_inicial = gerar_tabuleiro_inicial()
    tabuleiro_meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    #tabuleiro_inicial =  [[8, 2, 3], [4, 5, 6], [7, 1, 0]]
    print("Tabuleiro inicial:")
    imprimir_tabuleiro(tabuleiro_inicial)

    print("Tabuleiro final:")
    imprimir_tabuleiro(tabuleiro_meta)

    caminho = resolver_jogo_do_8(tabuleiro_inicial, tabuleiro_meta)
    if caminho:
        print("Solução encontrada em", len(caminho), "passos:")
        for movimento in caminho:
            print("Movimento:", movimento)
            tabuleiro_inicial = aplicar_movimento(tabuleiro_inicial, movimento)
            imprimir_tabuleiro(tabuleiro_inicial)
    else:
        print("Não foi possível encontrar uma solução.")

main()