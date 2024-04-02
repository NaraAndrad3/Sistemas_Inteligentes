
""" Controlar a dição de obstáculos: ex: eles não podem ficar sobrescritos e nem lado a lado """


import heapq
import matplotlib.pyplot as plt

class Node:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x # ---> Coordenada x e y
        self.y = coord_y
        self.cost = float('inf')   #----> o custo e a heuristica inicia com inf pq ainda não tem um valor associado e ele
        self.heuristic = float('inf')
        self.prev = None
    
    """ Esse método aqui compara dois nós e verifica se o custo + heuristica é maior ou menor, como a solução
    usa o algoritmo A* para encontrar a melhor solução, essa comparação é feita e o menor é seguido"""
    # def compare(self, other):
    #     return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

""" Essa função aqui calcula a heuristica entre o ponto atual e o ponto que se deseja chegar (distância de manhatam)"""
def calculate_heuristic(atual, objetivo):  
    return abs(atual.x - objetivo.x) + abs(atual.y - objetivo.y)

"""" Essa função encontra os vizinhos de um nó.
Ela recebe como parametro o nó atual e uma lista com a coordenada dos obstáculos,
a lista moves (movimentos) armazena todos os possiveis movimentos que o algoritmo pode fazer,
o loop for itera sobre os movimentos possiveis e atualiza a posição atual do no, em seguida verifica se 
essa nova coordenada está dentroda lista de obstáculos, se não estiver, ele é adicionado à lista neighbors (vizinhos).
"""
def neighbors(node, obstacles):
    neighbors = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] 
    for dx, dy in moves:
        new_x, new_y = node.x + dx, node.y + dy # -----> esse cálculo vai atualizar a posição do 'bonequin' pra poder verificar se o movimento é válido
        if (new_x, new_y) not in obstacles: # ------> se essa coordenada não estiver dentro da lista de obstáculos, ele é adicionado como vizinho
            neighbors.append(Node(new_x, new_y))
    return neighbors


def a_star(start, goal, obstacles):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)
    start.cost = 0
    start.heuristic = calculate_heuristic(start, goal)

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == (goal.x, goal.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.prev
            return path[::-1]

        closed_set.add((current.x, current.y))

        for neighbor in neighbors(current, obstacles):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            tentative_g = current.cost + 1
            if tentative_g < neighbor.cost:
                neighbor.prev = current
                neighbor.cost = tentative_g
                neighbor.heuristic = calculate_heuristic(neighbor, goal)
                heapq.heappush(open_list, neighbor)

    return None


def plot_grid(obstacles, path):
    fig, ax = plt.subplots()

    for obstacle in obstacles:
        ax.add_patch(plt.Rectangle((obstacle[0], obstacle[1]), 1, 1, color='gray'))

    if path:
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            ax.plot([x1 + 0.5, x2 + 0.5], [y1 + 0.5, y2 + 0.5], color='blue')

    ax.set_xticks(range(12))  # Define os ticks do eixo x em incrementos de 1
    ax.set_yticks(range(12))  # Define os ticks do eixo y em incrementos de 1
    
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


def main():
    start = Node(0, 0)
    goal = Node(10, 10)
    obstacles = {(2, 3), (3, 3), (6, 4), (5, 5),(1,1)}  # Exemplo de obstáculos

    path = a_star(start, goal, obstacles)
    if path:
        print("Caminho encontrado:")
        print(path)
        plot_grid(obstacles, path)
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    main()



