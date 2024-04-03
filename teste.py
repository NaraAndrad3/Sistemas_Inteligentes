from collections import deque
import matplotlib.pyplot as plt
import random

class No:
    def __init__(self, coord_x, coord_y, ant=None):
        self.x = coord_x
        self.y = coord_y
        self.ant = ant

def gerar_obstaculos_aleatorios(tamanho_grade, num_obstaculos, inicio, destino):
    obstaculos = set()
    while len(obstaculos) < num_obstaculos:
        x = random.randint(0, tamanho_grade - 1)
        y = random.randint(0, tamanho_grade - 1)
        if (x, y) != (inicio.x, inicio.y) and (x, y) != (destino.x, destino.y):
            obstaculos.add((x, y))
    return obstaculos

def obter_vizinhos(no, tamanho_grade, obstaculos):
    movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    vizinhos = []
    
    for dx, dy in movimentos:
        novo_x, novo_y = no.x + dx, no.y + dy
        if 0 <= novo_x < tamanho_grade and 0 <= novo_y < tamanho_grade and (novo_x, novo_y) not in obstaculos:
            vizinhos.append(No(novo_x, novo_y, ant=no))
    return vizinhos

def bfs(inicio, destino, tamanho_grade, obstaculos):
    visitados = set()
    fila = deque([inicio])
    
    while fila:
        atual = fila.popleft()
        if (atual.x, atual.y) == (destino.x, destino.y):
            caminho = []
            while atual:
                caminho.append((atual.x, atual.y))
                atual = atual.ant
            return caminho[::-1]
        
        if (atual.x, atual.y) not in visitados:
            visitados.add((atual.x, atual.y))
            vizinhos = obter_vizinhos(atual, tamanho_grade, obstaculos)
            fila.extend(vizinhos)
    
    return None

def plotar_grade(tamanho_grade, obstaculos, caminho=None):
    fig, ax = plt.subplots()
    
    for obs in obstaculos:
        ax.add_patch(plt.Rectangle((obs[0], obs[1]), 1, 1, color='grey'))
    
    if caminho:
        x_valores, y_valores = zip(*caminho)
        ax.plot(x_valores, y_valores, color='blue')
    
    ax.set_xticks(range(tamanho_grade))
    ax.set_yticks(range(tamanho_grade))
    ax.set_xlim(0, tamanho_grade)
    ax.set_ylim(0, tamanho_grade)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def principal():
    tamanho_grade = 21
    inicio = No(0, 0)
    destino = No(20, 20)
    obstaculos = gerar_obstaculos_aleatorios(tamanho_grade, 100, inicio, destino)
    caminho = bfs(inicio, destino, tamanho_grade, obstaculos)
    
    if caminho:
        print("Caminho encontrado:")
        print(caminho)
        plotar_grade(tamanho_grade, obstaculos, caminho)
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    principal()
